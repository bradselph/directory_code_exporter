# Project Structure and Code Extractor

## Overview

This script generates a comprehensive Markdown file detailing the structure and contents of a code project. It provides an overview of project files and directories, and includes the full contents of each file formatted with proper syntax highlighting.

## Features

- **Project Information**: Summary of total files, directories, and lines of code.
- **Directory Structure**: Hierarchical view of the project's directory and files with links to file contents.
- **File Contents**: Full content of each file, formatted with syntax highlighting.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/bradselph/project-structure-extractor.git
    ```

2. Navigate to the project directory:

    ```bash
    cd project-structure-extractor
    ```

## Usage

1. Run the script:

    ```bash
    python ProExtractor.py
    ```

2. Follow the prompts:
    - Enter the project name.
    - Enter the path to the project directory.
    - Specify the output file name (optional; defaults to `<project_name>_structure_with_code.md`).

3. The script will generate a Markdown file with the project's structure and file contents.

## License

This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Markdown](https://www.markdownguide.org/) for its clean formatting and readability.

# Example output

---
````
# Project Information

- **Total files**: 15
- **Total directories**: 7
- **Total code files**: 10
- **Total lines of code**: 200

## File Types and Counts

- `.py`: 4
- `.js`: 3
- `.html`: 2
- `.css`: 1
- `.md`: 1
- `No extension`: 4 (excluded files)

---

## Directory Structure

```
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── test_main.py
│   └── test_helpers.py
├── docs/
│   ├── index.html
│   └── styles.css
└── README.md
```

---

## File Contents

### [src/__init__.py](#src_initpy)

```python
# src/__init__.py
# Initialization of the src package
```

### [src/main.py](#src_mainpy)

```python
# src/main.py
def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    main()
```

### [src/utils/helpers.py](#src_util_helperspy)

```python
# src/utils/helpers.py
def helper_function():
    return "Helper function"
```

### [tests/test_main.py](#tests_test_mainpy)

```python
# tests/test_main.py
import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), None)
```

### [docs/index.html](#docs_indexhtml)

```html
<!-- docs/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project Documentation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Project Documentation</h1>
    <p>Welcome to the project documentation.</p>
</body>
</html>
```

### [docs/styles.css](#docs_stylescss)

```css
/* docs/styles.css */
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
}
```

### [README.md](#readmemd)

```markdown
# README.md
This is the README file for the project.
```

---

**Note:** Files with binary or image content, such as `.exe` or `.jpg`, are noted as excluded and do not have their contents displayed.
````