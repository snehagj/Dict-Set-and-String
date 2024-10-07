def string_operations():
    """Performs various operations on strings."""

    string = "Hello, world!"

    print("Original string:", string)

    # String functions
    print("String functions:")

    # Accessing characters
    print("First character:", string[0])
    print("Last character:", string[-1])

    # Slicing
    substring = string[1:4]
    print("Substring from 1 to 4:", substring)

    # Concatenation
    new_string = string + " How are you?"
    print("Concatenated string:", new_string)

    # Upper case
    uppercase = string.upper()
    print("Upper case:", uppercase)

    # Lower case
    lowercase = string.lower()
    print("Lower case:", lowercase)

    # Length
    length = len(string)
    print("Length of string:", length)

    # Split
    words = string.split()
    print("Split into words:", words)

    # Join
    joined_string = " ".join(words)
    print("Joined string:", joined_string)

    # Strip
    stripped_string = string.strip("!")
    print("Stripped string:", stripped_string)

    # Lstrip
    lstripped_string = string.lstrip("H")
    print("Left stripped string:", lstripped_string)

    # Rstrip
    rstipped_string = string.rstrip("!")
    print("Right stripped string:", rstipped_string)

    # Replace
    replaced_string = string.replace("world", "Python")
    print("Replaced string:", replaced_string)

    # Find
    index = string.find("world")
    print("Index of 'world':", index)

    # Index
    index = string.index("world")
    print("Index of 'world':", index)

    # Count
    count = string.count("o")
    print("Count of 'o':", count)

    # Startswith
    starts_with = string.startswith("Hello")
    print("Starts with 'Hello':", starts_with)

    # Endswith
    ends_with = string.endswith("!")
    print("Ends with '!':", ends_with)

    # Partition
    partitioned_string = string.partition("world")
    print("Partitioned string:", partitioned_string)

    # Rpartition
    rpartitioned_string = string.rpartition("world")
    print("Right partitioned string:", rpartitioned_string)

    # Splitlines
    splitlines_string = string.splitlines()
    print("Split into lines:", splitlines_string)

    # Isalpha
    is_alpha = string.isalpha()
    print("Is string alphabetic?", is_alpha)

    # Isdigit
    is_digit = string.isdigit()
    print("Is string digit?", is_digit)

    # Isalnum
    is_alnum = string.isalnum()
    print("Is string alphanumeric?", is_alnum)

    # Islower
    is_lower = string.islower()
    print("Is string lower case?", is_lower)

    # Isupper
    is_upper = string.isupper()
    print("Is string upper case?", is_upper)

    # Istitle
    is_title = string.istitle()
    print("Is string title case?", is_title)

    # Isspace
    is_space = string.isspace()
    print("Is string space?", is_space)

string_operations()