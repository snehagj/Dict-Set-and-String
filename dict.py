def dictionary_operations():
    """Performs various operations on dictionaries."""

    dictionary = {"name": "Rekha", "age": 20, "city": "Delhi"}

    # Accessing elements
    print(dictionary["name"])  # Get value by key

    # Updating elements
    dictionary["age"] = 21
    print(dictionary)

    # Deleting elements
    del dictionary["city"]
    print(dictionary)

    # Dictionary functions
    print("Dictionary functions:")

    # Get all keys
    keys = dictionary.keys()
    print("Keys:", keys)

    # Get all values
    values = dictionary.values()
    print("Values:", values)

    # Get all items (key-value pairs)
    items = dictionary.items()
    print("Items:", items)

    # Check if key exists
    print("Is 'name' a key?", "name" in dictionary)

    # Get length of dictionary
    print("Length of dictionary:", len(dictionary))

    # Clear dictionary
    dictionary.clear()
    print("Dictionary after clearing:", dictionary)

    # Create a copy of dictionary
    dictionary_copy = dictionary.copy()
    print("Copied dictionary:", dictionary_copy)

    # Get value by key, with default value if key doesn't exist
    print("Get value by key with default:", dictionary.get("age", "Not found"))

    # Pop an item from dictionary
    popped_item = dictionary.pop("age", "Not found")
    print("Popped item:", popped_item)

    # Update dictionary with another dictionary
    dictionary.update({"country": "India"})
    print("Updated dictionary:", dictionary)

    # Iterate over dictionary
    for key, value in dictionary.items():
        print("Key:", key, "Value:", value)

    # Iterate over keys
    for key in dictionary.keys():
        print("Key:", key)

    # Iterate over values
    for value in dictionary.values():
        print("Value:", value)

dictionary_operations()