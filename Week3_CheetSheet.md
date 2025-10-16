# Python Cheat Sheet: Control Flow, Dictionaries, and User Input

This cheat sheet covers `if` statements, dictionaries, user input, and `while` loops, corresponding to chapters 5, 6, and 7.

---

## Chapter 5: If Statements

Conditional statements allow your program to respond to different situations.

### Conditional Tests

* **Equality (`==`) and Inequality (`!=`)**
    Tests if two values are equal or not. The comparison is case-sensitive.

    ```python
    person = 'Sara'
    print(person == 'Sara')
    # Output: True

    print(person == 'John')
    # Output: False

    print(person != 'John')
    # Output: True
    ```

* **Case-Insensitive Equality Check**
    Use the `.lower()` method to ignore capitalization.

    ```python
    person = 'Sara'
    print(person.lower() == 'sara')
    # Output: True
    ```

* **Numerical Comparisons**
    Standard mathematical comparisons can be used.

    ```python
    temperature = -5
    # Check if water is freezing
    print(temperature < 0)
    # Output: True

    temperature = 110
    # Check if water is boiling
    print(temperature >= 100)
    # Output: True
    ```

* **Multiple Conditions (`and`, `or`)**
    Combine tests to check for multiple conditions.

    ```python
    # Check for a pleasant room temperature
    temperature = 20
    if temperature >= 15 and temperature <= 25:
        print("It's a pleasant room temperature.")
    # Output: It's a pleasant room temperature.
    ```

* **Checking for a Value in a List (`in`, `not in`)**

    ```python
    rooms = ['kitchen', 'living room', 'bedroom']
    print('bathroom' in rooms)
    # Output: False

    print('bathroom' not in rooms)
    # Output: True
    ```

### If Statement Structures

* **`if-else` Statement**
    Executes one block if the condition is true, and another if it's false. A simple pass/fail check.

    ```python
    grade = 55
    if grade > 50:
        print("You passed!")
    else:
        print("You failed.")
    # Output: You passed!
    ```

* **`if-elif-else` Chain**
    Tests a series of conditions in order to assign a letter grade.

    ```python
    score = 75
    if score >= 70:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'Fail'
    print(f"Your grade is {grade}.")
    # Output: Your grade is A.
    ```

* **Testing Multiple Conditions**
    Use a series of independent `if` statements if more than one block of code might need to run.

    ```python
    hobbies = ['reading', 'hiking']
    if 'reading' in hobbies:
        print("You enjoy reading.")
    if 'gaming' in hobbies:
        print("You enjoy gaming.")
    if 'hiking' in hobbies:
        print("You enjoy hiking.")
    # Output:
    # You enjoy reading.
    # You enjoy hiking.
    ```

---

## Chapter 6: Dictionaries

Dictionaries store information as key-value pairs.

### Working with Dictionaries

* **Creating a Dictionary**

    ```python
    person_0 = {'name': 'Sara', 'age': 25}
    ```

* **Accessing Values**
    Use the key in square brackets `[]`.

    ```python
    print(person_0['name'])
    # Output: Sara
    ```

* **Adding New Key-Value Pairs**

    ```python
    person_0['city'] = 'New York'
    print(person_0)
    # Output: {'name': 'Sara', 'age': 25, 'city': 'New York'}
    ```

* **Modifying Values**

    ```python
    person_0['age'] = 26
    print(person_0)
    # Output: {'name': 'Sara', 'age': 26, 'city': 'New York'}
    ```

* **Removing Key-Value Pairs**

    ```python
    del person_0['age']
    print(person_0)
    # Output: {'name': 'Sara', 'city': 'New York'}
    ```

* **Using `get()` for Safe Access**
    Avoid errors if a key might not exist.

    ```python
    profession = person_0.get('profession', 'No profession assigned.')
    print(profession)
    # Output: No profession assigned.
    ```

### Looping Through a Dictionary

* **Looping Through Key-Value Pairs**

    ```python
    person_details = {'username': 'sara_d', 'first': 'sara'}
    for key, value in person_details.items():
        print(f"Key: {key}, Value: {value}")
    ```

* **Looping Through Keys (`.keys()` or default)**

    ```python
    for key in person_details.keys():
        print(key.title())
    ```

* **Looping Through Values (`.values()`)**

    ```python
    for value in person_details.values():
        print(value.upper())
    ```

### Nesting

* **List of Dictionaries**

    ```python
    person_0 = {'name': 'Sara', 'age': 25}
    person_1 = {'name': 'John', 'age': 30}
    people = [person_0, person_1]
    ```

* **List in a Dictionary**

    ```python
    person = {
        'name': 'Sara',
        'hobbies': ['reading', 'hiking', 'coding'],
    }
    ```

* **Dictionary in a Dictionary**

    ```python
    users = {
        'sara_d': {'first': 'sara', 'last': 'davis', 'location': 'new york'},
        'john_s': {'first': 'john', 'last': 'smith', 'location': 'london'},
    }
    ```

---

## Chapter 7: User Input and `while` Loops

Make your programs interactive.

### Accepting User Input

* **The `input()` Function**
    Pauses the program and waits for the user to enter text.

    ```python
    message = input("Tell me something: ")
    print(f"You said: {message}")
    ```

* **Accepting Numerical Input**
    Use `int()` to convert the input string to an integer.

    ```python
    age = input("How old are you? ")
    age = int(age)
    if age >= 21:
        print("You can enter.")
    ```

* **The Modulo Operator (`%`)**
    Returns the remainder of a division. Useful for checking if a number is even or odd.

    ```python
    number = input("Enter a number: ")
    number = int(number)
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    ```

### `while` Loops

* **Basic `while` Loop**
    Runs as long as a condition remains true.

    ```python
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1
    # Output: 1 2 3 4 5
    ```

* **Letting the User Choose When to Quit**

    ```python
    prompt = "Enter 'quit' to end the program. "
    message = ""
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print(message)
    ```

* **Using a Flag**
    A variable that acts as a signal to control the loop's execution.

    ```python
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)
    ```

* **Using `break` to Exit a Loop**

    ```python
    while True:
        city = input("Please enter a city name: ")
        if city == 'quit':
            break
        else:
            print(f"I'd love to go to {city.title()}!")
    ```

* **Using `continue` in a Loop**
    Skips the rest of the current iteration and returns to the start of the loop.

    ```python
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)
    # Output: 1 3 5 7 9
    ```

* **Using a `while` Loop with Lists**
    Modify lists as you loop through them.

    ```python
    # Move items from one list to another
    unconfirmed = ['alice', 'brian']
    confirmed = []
    while unconfirmed:
        current_user = unconfirmed.pop()
        confirmed.append(current_user)
    print(confirmed)
    # Output: ['brian', 'alice']
    ```
