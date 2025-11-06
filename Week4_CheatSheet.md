# Python Cheat Sheet: Functions

This cheat sheet summarizes key concepts for defining and using functions in Python, based on Chapter 8.

---

## Chapter 8: Functions

Functions are named blocks of code designed to do one specific job.

### Defining and Calling a Function

* **Define a Simple Function**
    Use the `def` keyword. A `docstring` (in triple quotes) explains what the function does.
    ```python
    def greet_user():
        """Display a simple greeting."""
        print("Hello!")
    ```

* **Call a Function**
    Use the function's name followed by parentheses.
    ```python
    greet_user()
    # Output: Hello!
    ```

* **Parameter vs. Argument**
    -   **Parameter:** The variable in the function's definition (e.g., `username`).
    -   **Argument:** The value passed to the function when it's called (e.g., `'jesse'`).

    ```python
    def greet_user_by_name(username): # username is a parameter
        """Display a personalized greeting."""
        print(f"Hello, {username.title()}!")

    greet_user_by_name('jesse') # 'jesse' is an argument
    # Output: Hello, Jesse!
    ```

### Passing Arguments

* **Positional Arguments**
    Arguments are matched to parameters based on their order.
    ```python
    def describe_pet(animal_type, pet_name):
        """Display information about a pet."""
        print(f"\nI have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name.title()}.")

    describe_pet('hamster', 'harry')
    # Output:
    # I have a hamster.
    # My hamster's name is Harry.
    ```

* **Keyword Arguments**
    Name-value pairs passed to a function. Order doesn't matter.
    ```python
    describe_pet(animal_type='hamster', pet_name='harry')
    describe_pet(pet_name='harry', animal_type='hamster') # Same output
    ```

* **Default Values**
    Parameters can have default values. Parameters with defaults *must* come after parameters without them.
    ```python
    def describe_pet(pet_name, animal_type='dog'):
        """Display information about a pet."""
        print(f"\nI have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name.title()}.")
    
    # Call using the default value
    describe_pet(pet_name='willie')
    # Output:
    # I have a dog.
    # My dog's name is Willie.

    # Call overriding the default value
    describe_pet(pet_name='harry', animal_type='hamster')
    # Output:
    # I have a hamster.
    # My hamster's name is Harry.
    ```

### Return Values

Functions can process data and `return` a value.

* **Return a Simple Value**
    ```python
    def get_formatted_name(first_name, last_name):
        """Return a full name, neatly formatted."""
        full_name = f"{first_name} {last_name}"
        return full_name.title()

    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)
    # Output: Jimi Hendrix
    ```

* **Make an Argument Optional**
    Use a default value (like an empty string `''`) to make an argument optional.
    ```python
    def get_formatted_name(first_name, last_name, middle_name=''):
        """Return a full name, neatly formatted."""
        if middle_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"
        return full_name.title()

    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)
    # Output: Jimi Hendrix

    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician)
    # Output: John Lee Hooker
    ```

* **Return a Dictionary**
    You can return any data type, like a dictionary. Use `None` for optional values.
    ```python
    def build_person(first_name, last_name, age=None):
        """Return a dictionary of information about a person."""
        person = {'first': first_name, 'last': last_name}
        if age:
            person['age'] = age
        return person

    musician = build_person('jimi', 'hendrix', age=27)
    print(musician)
    # Output: {'first': 'jimi', 'last': 'hendrix', 'age': 27}
    ```

### Passing a List

* **Pass a List to a Function**
    The function gets access to the list's contents.
    ```python
    def greet_users(names):
        """Print a simple greeting to each user in the list."""
        for name in names:
            msg = f"Hello, {name.title()}!"
            print(msg)

    usernames = ['hannah', 'ty', 'margot']
    greet_users(usernames)
    # Output:
    # Hello, Hannah!
    # Hello, Ty!
    # Hello, Margot!
    ```

* **Modify a List in a Function**
    Changes made to the list inside the function are permanent.
    ```python
    unprinted = ['phone case', 'robot']
    completed = []

    def print_models(unprinted_designs, completed_models):
        """Simulate printing, moving each design to completed_models."""
        while unprinted_designs:
            current_design = unprinted_designs.pop()
            print(f"Printing model: {current_design}")
            completed_models.append(current_design)
    
    print_models(unprinted, completed)
    print(f"Unprinted: {unprinted}")
    print(f"Completed: {completed}")
    # Output:
    # Printing model: robot
    # Printing model: phone case
    # Unprinted: []
    # Completed: ['robot', 'phone case']
    ```

* **Prevent Modifying a List**
    Pass a *copy* of the list using slice notation `[:]`.
    ```python
    original_list = ['a', 'b', 'c']
    completed_list = []
    
    # Passing a copy [:] leaves the original list unchanged
    print_models(original_list[:], completed_list) 
    
    print(f"Original: {original_list}")
    # Output: Original: ['a', 'b', 'c']
    ```

### Arbitrary Number of Arguments

* **Arbitrary Positional Arguments (`*args`)**
    The `*` packs arguments into a *tuple*. Often named `*args`.
    ```python
    def make_pizza(size, *toppings):
        """Summarize the pizza being ordered."""
        print(f"\nMaking a {size}-inch pizza with the following toppings:")
        for topping in toppings:
            print(f"- {topping}")

    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
    # Output:
    # Making a 16-inch pizza with the following toppings:
    # - pepperoni
    #
    # Making a 12-inch pizza with the following toppings:
    # - mushrooms
    # - green peppers
    # - extra cheese
    ```

* **Arbitrary Keyword Arguments (`**kwargs`)**
    The `**` packs arguments into a *dictionary*. Often named `**kwargs`.
    ```python
    def build_profile(first, last, **kwargs):
        """Build a dictionary containing user info."""
        # create the empty user info dictionary
        user_info = {}
    
        # add first and last name items
        user_info['first_name'] = first
        user_info['last_name'] = last

        # add the additional key value pairs from the kwargs
        for key,value in kwargs.items():
            user_info[key] = value
        return user_info

    user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
    print(user_profile)
    # Output: {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
    ```

* **Arbitrary mixture of arguments (`*args`) and Keyword Arguments (`**kwargs`)**
    ```python
    def print_arguments(*args, **kwargs):
        # print non-keyword argments
        for item in args:
            print(f"argument: {item}")
        for key, value in kwargs.items():
            print(f"keyword argument: {key} = {value}")
        return

    print_arguments(10, 20, name="Albert", loc="US")
    # Output:
    # argument: 10
    # argument: 20
    # keyword argument: name = Albert
    # keyword argument: loc = US
    ```

### Storing Functions in Modules

* **Import an Entire Module**
    (Assumes functions are in a file named `pizza.py`)
    ```python
    import pizza

    pizza.make_pizza(16, 'pepperoni')
    ```

* **Import a Specific Function**
    ```python
    from pizza import make_pizza

    make_pizza(16, 'pepperoni')
    ```

* **Give a Function an Alias (`as`)**
    ```python
    from pizza import make_pizza as mp

    mp(16, 'pepperoni')
    ```

* **Give a Module an Alias (`as`)**
    ```python
    import pizza as p

    p.make_pizza(16, 'pepperoni')
    ```

* **Import All Functions (Not Recommended)**
    Can cause name conflicts.
    ```python
    from pizza import *

    make_pizza(16, 'pepperoni')
    ```
