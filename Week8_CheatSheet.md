# Python File Management Cheat Sheet

### 1. Path Fundamentals & Properties (`pathlib.Path`)

The `pathlib` module is the modern, cross-platform way to manage file paths.

| Operation | Description | Example |
| :--- | :--- | :--- |
| `from pathlib import Path` | Imports the core class. | `from pathlib import Path` |
| `Path("filename")` | Creates a **Path object**. | `p = Path("data/report.txt")` |
| `path / "subpath"` | **Joins path parts** (cross-platform). | `p = Path.home() / "documents"` |
| `Path.cwd()` | Gets the **C**urrent **W**orking **D**irectory. | `cwd = Path.cwd()` |
| `Path.home()` | Gets the user's **home directory**. | `home = Path.home()` |
| `path.resolve()` | Converts a path to its full, **absolute path**. | `abs_path = p.resolve()` |

#### Path Components

Methods for breaking down a file path into its parts.

| Method | Description | Example |
| :--- | :--- | :--- |
| `path.name` | The **full filename** (basename + extension). | `'report.txt'` |
| `path.stem` | The **base name** _without_ the extension. | `'report'` |
| `path.suffix` | The **file extension**, including the dot. | `'.txt'` |
| `path.parent` | The **containing directory**. | `p.parent` |

---

### 2. Checks, Status, and Components

Methods for checking the existence and type of a file system entry.

| Method | Returns | Description |
| :--- | :--- | :--- |
| **`path.exists()`** | `True` or `False` | Checks if the file or directory exists. |
| **`path.is_file()`** | `True` or `False` | Checks if the path refers to a regular file. |
| **`path.is_dir()`** | `True` or `False` | Checks if the path refers to a directory (folder). |

---

### 3. File & Directory Management Operations

| Operation | Method | Notes |
| :--- | :--- | :--- |
| **Create Directory** | `Path("new_folder").mkdir()` | Use `exist_ok=True` to suppress errors if it exists. |
| **Remove Empty Dir** | `Path("temp_folder").rmdir()` | **Removes an empty directory.** |
| **Change Directory** | `os.chdir('data')` | **Warning:** Changes the global Current Working Directory. Requires `import os`. |
| **Delete File** | `Path("old_data.txt").unlink()` | **Deletes the file.** |
| **List Directory** | `p.iterdir()` | Iterates over all files/folders in directory `p`. |
| **Glob (Recursive)** | `p.rglob("*.txt")` | Finds items matching the pattern in all subfolders. |

---

### 4. Reading and Writing Content by Format

#### A. Plain Text Files (`.txt`, `.py`, `.log`, `.md`)

| Operation | Method | Example Code |
| :--- | :--- | :--- |
| **Read Content** | `path.read_text()` | `content = Path("file.txt").read_text()` |
| **Write Content** | `path.write_text(content)` | `Path("file.txt").write_text("New data\n")` |

##### Content Processing

| Operation | Method | Example Code |
| :--- | :--- | :--- |
| **Split into Lines** | `content.splitlines()` | `lines = content.splitlines()` |
| **Split Lines to Items** | `line.split(delimiter)` | `items = line.split(',')` |
| **Convert to Int** | `int(string_value)` | `number = int(items[0])` |
| **Convert to Float** | `float(string_value)` | `price = float(items[1])` |

#### B. Nested Data (Hierarchical Structures)

##### JSON (`json` module)

**Read/Decode**

```python
content = Path("user.json").read_text()
json_obj = json.loads(content)

# one line
json_obj = json.loads(Path("user.json").read_text())
```

**Write/Encode**

```python
data_struct = [ { 'data': [ 91,223,9,32 ]}, "12-3-99" } ]

# save to json format
json_str = json.dumps(data_struct)
Path("example.json").write_text(json_str)

# one line
Path("example.json").write_text(json.dumps(data_struct))
```

##### XML (`xml.etree` module)

| Operation | Module | Example Code |
| :--- | :--- | :--- |
| **Read/Parse** | `xml.etree` | `tree = ElementTree.parse('data.xml')` |
| **Write/Output** | `xml.etree` | `tree.write('new_data.xml')` |
| **Note** | | **XML parsing will NOT be examined in this course and is non-examinable.** |

#### C. Tabular Data: Importing Directly into Pandas (`DataFrame`)

Use `pandas` for reading and writing data that represents a table (requires `import pandas as pd`).

| Data Format | Pandas Function | Write Operation |
| :--- | :--- | :--- |
| **CSV** | `pd.read_csv("data.csv")` | `df.to_csv("output.csv")` |
| **JSON** | `pd.read_json("data.json")` | `df.to_json("output.json")` |
| **XML** | `pd.read_xml("data.xml")` | `df.to_xml("output.xml")` |
| **HTML** | `pd.read_html("page.html")` | `df.to_html("output.html")` |

---

### 5. Safety and Exception Handling

An **Exception** occurs when an issue halts normal program flow. Use `try...except` to anticipate and manage these.

| Type | Common Cause | Handling Strategy |
| :--- | :--- | :--- |
| **I/O Error** | File not found, corrupted, or permission denied. | `try...except FileNotFoundError` block. |
| **Data Error** | Missing keys (`KeyError`) or invalid data types (`TypeError`). | `Use specific except blocks.` |
| **Raising Error** | Manually stopping program execution due to invalid data/state. | `if val < 0: raise Exception("Value must be positive")` |

**Critical Safety Warning:**

* Python runs with your **user permissions**. Code has the potential to delete or modify data.
* When using `path.write_text()` or `path.unlink()`, **there is no undo button**.
* **Back up your work**! Always review untrusted code.
