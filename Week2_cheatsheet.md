
# Python Cheat Sheet: Lists & Loops

This cheat sheet summarizes key commands for working with lists and loops in Python.

https://g.co/gemini/share/3bd11baf8e38

---

## Chapter 3: Introducing Lists

### Creating and Accessing Lists

* **Create a List**
    A collection of items in a specific order, enclosed in square brackets `[]`.
    ```python
    mylist = ['apple', 'bread', 'cake']
    ```

* **Create an Empty List**
    ```python
    empty_list = []
    ```

* **Access an Element by Index**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist[0]
    # Output: 'apple'
    ```
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist[2]
    # Output: 'cake'
    ```

* **Access the Last Element**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist[-1]
    # Output: 'cake'
    ```

### Modifying, Adding, and Removing Elements

* **Modify an Element**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist[1] = 'donut'
    print(mylist)
    # Output: ['apple', 'donut', 'cake']
    ```

* **Append an Element (to the end)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist.append('donut')
    print(mylist)
    # Output: ['apple', 'bread', 'cake', 'donut']
    ```

* **Insert an Element (at a position)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist.insert(1, 'biscuit')
    print(mylist)
    # Output: ['apple', 'biscuit', 'bread', 'cake']
    ```

* **Remove with `del` (by position)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    del mylist[1]
    print(mylist)
    # Output: ['apple', 'cake']
    ```

* **Remove with `pop()` (from the end)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    popped_item = mylist.pop()
    
    print(popped_item)
    # Output: cake
    
    print(mylist)
    # Output: ['apple', 'bread']
    ```

* **Remove with `pop()` (by position)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    popped_item = mylist.pop(1)

    print(popped_item)
    # Output: bread

    print(mylist)
    # Output: ['apple', 'cake']
    ```

* **Remove with `remove()` (by value)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist.remove('bread')
    print(mylist)
    # Output: ['apple', 'cake']
    ```

### Organizing a List

* **Sort a List Permanently (`sort`)**
    ```python
    mylist = ['cake', 'apple', 'bread']
    mylist.sort()
    print(mylist)
    # Output: ['apple', 'bread', 'cake']
    ```
    ```python
    mylist = ['cake', 'apple', 'bread']
    mylist.sort(reverse=True)
    print(mylist)
    # Output: ['cake', 'bread', 'apple']
    ```

* **Sort a List Temporarily (`sorted`)**
    ```python
    mylist = ['cake', 'apple', 'bread']
    
    print(sorted(mylist))
    # Output: ['apple', 'bread', 'cake']
    
    print(mylist)
    # Output: ['cake', 'apple', 'bread']
    ```

* **Reverse a List's Order (`reverse`)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist.reverse()
    print(mylist)
    # Output: ['cake', 'bread', 'apple']
    ```

* **Find the Length of a List (`len`)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    len(mylist)
    # Output: 3
    ```

---

## Chapter 4: Working with Lists

### Looping Through a List

* **`for` Loop**
    ```python
    mylist = ['apple', 'bread', 'cake']
    for item in mylist:
        print(item)
    # Output:
    # apple
    # bread
    # cake
    ```

* **Loop with Index (`enumerate`)**
    ```python
    mylist = ['apple', 'bread', 'cake']
    for index, item in enumerate(mylist):
        print(f"Index: {index}, Item: {item}")
    # Output:
    # Index: 0, Item: apple
    # Index: 1, Item: bread
    # Index: 2, Item: cake
    ```

### Making Numerical Lists

* **Generate a Sequence of Numbers (`range`)**
    ```python
    # Counts from 1 up to (but not including) 5
    for value in range(1, 5):
        print(value)
    # Output:
    # 1
    # 2
    # 3
    # 4
    ```
    ```python
    # Starts from 0 by default
    for value in range(6):
        print(value)
    # Output:
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    ```

* **Create a List of Numbers from `range`**
    ```python
    numbers = list(range(1, 6))
    print(numbers)
    # Output: [1, 2, 3, 4, 5]
    ```

* **Simple Statistics**
    ```python
    # In a notebook, the result of the last line is automatically shown.
    numbers = [3, 7, 2, 8]
    
    min(numbers)
    # Output: 2
    
    max(numbers)
    # Output: 8
    
    sum(numbers)
    # Output: 20
    ```

* **List Comprehension**
    A compact way to create lists.
    ```python
    # Example with numbers from a list
    numbers = [3, 7, 2, 8]
    plus_one = [n + 1 for n in numbers]
    print(plus_one)
    # Output: [4, 8, 3, 9]
    ```
    ```python
    # Basic example: create a list of squares
    squares = [value**2 for value in range(1, 11)]
    print(squares)
    # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```
    ```python
    # Example with an operation on a list of strings
    mylist1 = ['apple', 'bread', 'cake']
    mylist2 = [item.upper() for item in mylist]
    print(mylist2)
    # Output: ['APPLE', 'BREAD', 'CAKE']
    ```

### Working with Part of a List (Slicing)

* **Create a Slice**
    ```python
    mylist = ['apple', 'bread', 'cake', 'donut', 'egg', 'fish']
    mylist[1:4]
    # Output: ['bread', 'cake', 'donut']
    ```

* **Slice from the Beginning**
    ```python
    mylist = ['apple', 'bread', 'cake', 'donut', 'egg', 'fish']
    mylist[:3]
    # Output: ['apple', 'bread', 'cake']
    ```

* **Slice to the End**
    ```python
    mylist = ['apple', 'bread', 'cake', 'donut', 'egg', 'fish']
    mylist[2:]
    # Output: ['cake', 'donut', 'egg', 'fish']
    ```

* **Copy a List**
    ```python
    mylist = ['apple', 'bread', 'cake']
    mylist_copy = mylist[:] # Make a copy

    mylist.append('donut')
    mylist_copy.append('egg')
    
    print(mylist)
    # Output: ['apple', 'bread', 'cake', 'donut']
    
    print(mylist_copy)
    # Output: ['apple', 'bread', 'cake', 'egg']
    ```

### Tuples (Immutable Lists)

* **Define a Tuple**
    Its items cannot be changed.
    ```python
    mytuple = ('red', 'green', 'blue')
    ```
    
* **Create an Empty Tuple**
    ```python
    empty_tuple = ()
    ```

* **Create a Tuple with One Element**
    A trailing comma is required.
    ```python
    single_item_tuple = ('red',)
    ```

* **Access an Element in a Tuple**
    ```python
    mytuple = ('red', 'green', 'blue')
    mytuple[1]
    # Output: 'green'
    ```

* **Attempt to Modify a Tuple (causes an error)**
    ```python
    mytuple = ('red', 'green', 'blue')
    mytuple[1] = 'purple'
    # Output:
    # TypeError: 'tuple' object does not support item assignment
    ```

* **Loop Through a Tuple**
    ```python
    mytuple = ('red', 'green', 'blue')
    for item in mytuple:
        print(item)
    # Output:
    # red
    # green
    # blue
    ```

* **Overwrite a Tuple**
    You can't change a tuple, but you can assign a new tuple to the variable.
    ```python
    mytuple = ('red', 'green', 'blue')
    mytuple = ('yellow', 'purple', 'pink')
    print(mytuple)
    # Output: ('yellow', 'purple', 'pink')
    ```
    
