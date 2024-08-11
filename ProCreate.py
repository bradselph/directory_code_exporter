import os

def recreate_project(directory_file, contents_file, output_path):
    """Recreates the project structure and files from directory and contents files."""
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Dictionary to keep track of folder paths
    folder_paths = {}
    
    # Process directory structure
    with open(directory_file, 'r', encoding='utf-8') as dir_file:
        for line in dir_file:
            line = line.strip()
            if line.endswith('/'):
                # Handle directory creation
                level = line.count('│   ')  # Determine the level of the directory
                parts = line.split('├── ')
                dir_name = parts[-1].strip('/ ')
                if level == 0:
                    dir_path = os.path.join(output_path, dir_name)
                else:
                    parent_dir = folder_paths.get(level - 1, output_path)
                    dir_path = os.path.join(parent_dir, dir_name)
                folder_paths[level] = dir_path
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
    
    # Process file contents
    current_file_name = None
    file_content = []
    
    with open(contents_file, 'r', encoding='utf-8') as content_file:
        for line in content_file:
            if line.startswith('<') and line.endswith('>\n'):
                if current_file_name:
                    # Write content to the current file
                    with open(current_file_path, 'w', encoding='utf-8') as file:
                        file.write(''.join(file_content))
                # Start new file
                current_file_name = line[1:-2]
                # Determine the correct path for the new file
                file_parts = current_file_name.split('/')
                file_dir = os.path.join(output_path, *file_parts[:-1])
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                current_file_path = os.path.join(file_dir, file_parts[-1])
                file_content = []
            elif line.startswith(f'</{current_file_name}>'):
                if current_file_path:
                    # Write content to the current file
                    with open(current_file_path, 'w', encoding='utf-8') as file:
                        file.write(''.join(file_content))
                current_file_path = None
                file_content = []
            elif current_file_path:
                file_content.append(line)
        
        # Handle the last file if needed
        if current_file_path:
            with open(current_file_path, 'w', encoding='utf-8') as file:
                file.write(''.join(file_content))

if __name__ == "__main__":
    print("Welcome to the Project Reconstructor!")

    output_directory = 'reconstructed_project'
    
    print(f"Reconstructing project in '{output_directory}'...")
    
    recreate_project('directory.txt', 'contents.txt', output_directory)
    
    print(f"Reconstruction completed successfully in '{output_directory}'!")
