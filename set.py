def set_operations():
    """Performs various operations on sets."""

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    print("Set 1:", set1)
    print("Set 2:", set2)

    # Set functions
    print("Set functions:")

    # Union
    union_set = set1.union(set2)
    print("Union:", union_set)

    # Intersection
    intersection_set = set1.intersection(set2)
    print("Intersection:", intersection_set)

    # Difference
    difference_set = set1.difference(set2)
    print("Difference:", difference_set)

    # Symmetric Difference
    symmetric_difference_set = set1.symmetric_difference(set2)
    print("Symmetric Difference:", symmetric_difference_set)

    # Subset
    subset = set1.issubset(set2)
    print("Is set1 a subset of set2?", subset)

    # Superset
    superset = set1.issuperset(set2)
    print("Is set1 a superset of set2?", superset)

    # Disjoint
    disjoint = set1.isdisjoint(set2)
    print("Are set1 and set2 disjoint?", disjoint)

    # Add element
    set1.add(4)
    print("Set 1 after adding 4:", set1)

    # Update set
    set1.update({5, 6})
    print("Set 1 after updating:", set1)

    # Remove element
    set1.remove(4)
    print("Set 1 after removing 4:", set1)

    # Discard element
    set1.discard(5)
    print("Set 1 after discarding 5:", set1)

    # Pop element
    popped_element = set1.pop()
    print("Popped element:", popped_element)
    print("Set 1 after popping:", set1)

    # Clear set
    set1.clear()
    print("Set 1 after clearing:", set1)

    # Copy set
    set1_copy = set1.copy()
    print("Copied set:", set1_copy)

    # Convert list to set
    list1 = [1, 2, 2, 3, 4, 4, 5]
    set_from_list = set(list1)
    print("Set from list:", set_from_list)

set_operations()