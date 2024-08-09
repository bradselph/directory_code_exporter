import os
import re

# Define file extensions to be excluded from content extraction
EXCLUDED_EXTENSIONS = {'.exe', '.dll', '.bin', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico', '.svg'}
# Map file extensions to their corresponding Markdown syntax highlighting
LANGUAGE_MAP = {
    '.py': 'python',
    '.java': 'java',
    '.js': 'javascript',
    '.c': 'c',
    '.cpp': 'cpp',
    '.h': 'cpp',
    '.go': 'go',
    '.rb': 'ruby',
    '.php': 'php',
    '.html': 'html',
    '.css': 'css',
    '.ts': 'typescript',
    # Add more extensions as needed
}

def get_file_contents(filepath):
    """Reads and returns the contents of a file, or notes its exclusion if it's a binary file."""
    try:
        if os.path.splitext(filepath)[1].lower() in EXCLUDED_EXTENSIONS:
            return "Excluded file type (binary/image)"
        
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file {filepath}: {e}"

def collect_project_data(startpath):
    """Collects data about the project including file types, counts, and code lines."""
    file_count = 0
    dir_count = 0
    file_types = {}
    total_lines_of_code = 0
    file_paths = []
    
    def traverse_directory(root):
        nonlocal file_count, dir_count, file_types, total_lines_of_code, file_paths
        
        files = sorted(os.listdir(root))
        for f in files:
            file_path = os.path.join(root, f)
            if os.path.isdir(file_path):
                dir_count += 1
                traverse_directory(file_path)
            else:
                ext = os.path.splitext(f)[1].lower()
                file_types[ext] = file_types.get(ext, 0) + 1
                file_count += 1
                file_paths.append(file_path)
                
                if ext in EXCLUDED_EXTENSIONS:
                    continue
                
                content = get_file_contents(file_path)
                total_lines_of_code += content.count('\n') + 1
    
    traverse_directory(startpath)
    
    return file_count, dir_count, file_types, total_lines_of_code, file_paths

def get_language_extension(ext):
    """Returns the language for syntax highlighting based on the file extension."""
    return LANGUAGE_MAP.get(ext, 'text')

def format_anchor_name(filename):
    """Formats a file name into a Markdown-friendly anchor name."""
    return re.sub(r'[^\w\s]', '', filename).replace(' ', '_').lower()

def write_project_info(file, file_count, dir_count, file_types, total_lines_of_code):
    """Writes the project information to the file in Markdown format."""
    total_code_files = sum(count for ext, count in file_types.items() if ext in LANGUAGE_MAP)
    
    file.write(f"# Project Information\n\n")
    file.write(f"- **Total files**: {file_count}\n")
    file.write(f"- **Total directories**: {dir_count}\n")
    file.write(f"- **Total code files**: {total_code_files}\n")
    file.write(f"- **Total lines of code**: {total_lines_of_code}\n")
    
    file.write(f"\n## File Types and Counts\n")
    for ext, count in sorted(file_types.items()):
        file.write(f"- `{ext if ext else 'No extension'}`: {count}\n")
    
    file.write("\n")

def write_directory_structure(file, startpath):
    """Writes the directory structure to the file in Markdown format with links to file contents."""
    def write_structure_and_links(root, level, is_last):
        """Helper function to write directory structure recursively."""
        indent = ' ' * 4 * (level - 1)
        if level > 0:
            file.write(f"{indent}{'└── ' if is_last else '├── '}{os.path.basename(root)}/\n")
        
        subindent = ' ' * 4 * level
        files = sorted(os.listdir(root))
        last_index = len(files) - 1
        
        for i, f in enumerate(files):
            file_path = os.path.join(root, f)
            if os.path.isdir(file_path):
                write_structure_and_links(file_path, level + 1, i == last_index)
            else:
                ext = os.path.splitext(f)[1].lower()
                if ext not in EXCLUDED_EXTENSIONS:
                    anchor_name = format_anchor_name(f)
                    file.write(f"{subindent}{'└── '}[{f}](#{anchor_name})\n")
                else:
                    file.write(f"{subindent}{'└── '}{f} (Excluded)\n")
    
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write("## Directory Structure\n\n")
        write_structure_and_links(startpath, 0, True)
        file.write("\n")

def write_file_contents(file, startpath, file_paths):
    """Writes the contents of each file to the file in Markdown format with headers and code blocks."""
    def write_contents():
        """Helper function to write file contents recursively."""
        for file_path in file_paths:
            ext = os.path.splitext(file_path)[1].lower()
            lang = get_language_extension(ext)
            relative_path = os.path.relpath(file_path, startpath)
            anchor_name = format_anchor_name(relative_path)
            
            file.write(f"\n### [{relative_path}](#{anchor_name})\n")
            file.write(f"```{lang}\n")
            if ext in EXCLUDED_EXTENSIONS:
                file.write("Excluded file type (binary/image)\n")
            else:
                content = get_file_contents(file_path)
                file.write(content)
            file.write("```\n")
    
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write("## File Contents\n\n")
        write_contents()
        file.write("\n")

if __name__ == "__main__":
    print("Welcome to the Project Structure and Code Extractor!")
    
    project_name = input("Enter the project name: ").strip()
    project_path = input("Enter the path to your project directory: ").strip()
    output_file = input(f"Enter the name for the output Markdown file (default '{project_name}_structure_with_code.md'): ").strip()
    
    if not output_file:
        output_file = f'{project_name}_structure_with_code.md'
    elif not output_file.endswith('.md'):
        output_file += '.md'
    
    print(f"\nProcessing project '{project_name}' located at '{project_path}'...")
    
    # Collect project data
    file_count, dir_count, file_types, total_lines_of_code, file_paths = collect_project_data(project_path)
    
    print(f"\nCollecting data completed. Writing to '{output_file}'...")
    
    # Write project info
    with open(output_file, 'w', encoding='utf-8') as file:
        write_project_info(file, file_count, dir_count, file_types, total_lines_of_code)
    
    # Write directory structure
    write_directory_structure(output_file, project_path)
    
    # Write file contents
    write_file_contents(output_file, project_path, file_paths)
    
    print(f"\nProject information, structure, and code have been written to '{output_file}'")
    print("Process completed successfully!")
