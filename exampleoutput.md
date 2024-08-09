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