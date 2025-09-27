
# Python Cheat Sheet: Getting Started & Variables

This cheat sheet summarizes key commands for getting started with Python, including variables and simple data types.

---

## Getting Started

* **The `print()` Function**
    Used to display output to the screen.
    ```python
    print("Hello World!")
    # Output:
    # Hello World!
    ```

* **Running a Python File from the Terminal**
    You can execute a Python script saved in a file (e.g., `hello.py`).
    ```bash
    # On Windows
    python hello.py

    # On macOS/Linux
    python3 hello.py
    ```

---

## Variables & Simple Data Types

### Common Data Types
Python has several built-in data types. Here are the most common ones you'll start with.

* **Integer (`int`)**: Whole numbers, without decimals.
    ```python
    my_age = 25
    number_of_items = 100
    ```

* **Float (`float`)**: Numbers with a decimal point.
    ```python
    item_price = 19.99
    length_cm = 32.6
    ```

* **String (`str`)**: A sequence of characters (text).
    ```python
    user_name = "Peter Parker"
    greeting = 'Hello there!'
    ```

### Variables

A variable stores a value. Think of it as a label for data.

* **Assigning a Variable**
    ```python
    myname = "Peter Parker"
    print(myname)
    # Output:
    # Peter Parker
    ```
    ```python
    age = 19
    print(age)
    # Output:
    # 19
    ```

* **Multiple Assignment**
    Assign values to multiple variables in one line.
    ```python
    x, y, z = 0, 1, 2
    print(x)
    # Output: 0
    print(y)
    # Output: 1
    ```

* **Reassigning a Variable**
    You can change a variable's value at any time.
    ```python
    myname = "Spider-Man"
    print(myname)
    # Output: Spider-Man

    myname = "Green Goblin"
    print(myname)
    # Output: Green Goblin
    ```

* **Variable Naming Rules**
    - Can only contain letters, numbers, and underscores.
    - Must start with a letter or an underscore, not a number.
    - No spaces are allowed (use underscores instead).
    - Do not use names which already exist in Python, common mistakes include using: `sum`, `len`, `str`, `max`, `min`, `input`, `list`
    - Keep them short but descriptive (e.g., `user_name` is better than `un`).

* **Constants**
    A variable whose value should not be changed through the program. Convention is to use all caps.
    ```python
    MAX_CONNECTIONS = 5000
    ```


### Commenting your code

You should add comments to add useful notes that describe what is being done. You do not need comments if what the code does is already clear!

* **Adding Comments in Python**

    ```python
    # This is a comment explaining my code.
    print("Hello everyone!") # This is an inline comment.
    ```

### Strings (Text)

A series of characters, surrounded by single `'` or double `"` quotes.

* **Using and Escaping Quotes**
    ```python
    # You can use single or double quotes
    message1 = "My name is Peter Parker"
    message2 = 'I fight crime.'

    # You can use double quotes within a single quote string
    quote = 'Green Goblin said, "I will get you!"'
    print(quote)
    # Output: Green Goblin said, "I will get you!"
    
    # You can also use backslashes \ to escape a quote
    apostrophe = 'No you won\'t!'
    print(apostrophe)
    # Output: No you won't!
    ```
    
* **Triple Quotes (Multi-line Strings)**

  Python also allows you to define strings using triple quotes.  This lets you enter a clock of text, and because it is ended only by a triple quote, is useful if your text contains lots of quote marks.

    ```python
    mytext = """Peter said, "I'm Spider-Man,
    and you're going to jail."
    "Noooo!" said Green Goblin."""
    print(mytext)
    # Output:
    # Peter said, "I'm Spider-Man,
    # and you're going to jail."
    # "Noooo!" said Green Goblin.
    ```

* **Changing Case**
    ```python
    name = "peter parker"

    # Title case
    print(name.title())
    # Output: Peter Parker

    # Upper case
    print(name.upper())
    # Output: PETER PARKER

    # Lower case
    print(name.lower())
    # Output: peter parker
    ```

* **Using Variables in Strings (f-strings)**
    Prefix the string with an `f` and put variables in curly braces `{}`.
    ```python
    first_name = "peter"
    last_name = "parker"
    full_name = f"{first_name} {last_name}"
    print(full_name)
    # Output: peter parker

    message = f"Hello, {full_name.title()}!"
    print(message)
    # Output: Hello, Peter Parker!
    ```

* **Adding Tabs and Newlines**
    ```python
    # \t adds a tab
    print("\tPython")
    # Output:
    #     Python

    # \n adds a newline
    print("Characters:\n - Spider-Man\n - Green Goblin")
    # Output:
    # Characters:
    #  - Spider-Man
    #  - Green Goblin
    ```

* **Stripping Whitespace**
    ```python
    myhero = '  spider-man  '

    # Remove from right side
    myhero.rstrip()
    # Output: '  spider-man'

    # Remove from left side
    myhero.lstrip()
    # Output: 'spider-man  '

    # Remove from both sides
    myhero.strip()
    # Output: 'spider-man'
    ```

* **Removing Prefixes and Suffixes**
    ```python
    url = '[https://www.google.com](https://www.google.com)'
    url.removeprefix('https://')
    # Output: '[www.google.com](https://www.google.com)'

    filename = 'myfirstcode.py'
    filename.removesuffix('.py')
    # Output: 'myfirstcode'
    ```

### Numbers

* **Integers (whole numbers)**
    You can perform standard math operations.
    ```python
    # Addition
    2 + 3
    # Output: 5

    # Subtraction
    3 - 2
    # Output: 1

    # Multiplication
    2 * 3
    # Output: 6

    # Division (always results in a float)
    3 / 2
    # Output: 1.5
    ```

* **Exponents**
    Use two asterisks `**`.
    ```python
    3**2
    # Output: 9
    ```

* **Floats (numbers with decimals)**
    Python handles decimals automatically.
    ```python
    0.1 + 0.1
    # Output: 0.2

    2 * 0.2
    # Output: 0.4
    ```

* **Underscores in Numbers**
    For readability; Python ignores them.
    ```python
    universe_age = 14_000_000_000
    print(universe_age)
    # Output: 14000000000
    ```

* **Scientific (e) Notation**
    A compact way to write very large or very small numbers.
    ```python
    # 3 million (3 with 6 zeros)
    large_number = 3e6
    print(large_number)
    # Output: 3000000.0

    # 0.02
    small_number = 2e-2
    print(small_number)
    # Output: 0.02
    ```




    
