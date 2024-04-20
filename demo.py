def main():
    # Creating a list
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)

    # Adding elements to list
    my_list.append(6)
    print("List after adding element:", my_list)

    # Removing an element from list
    my_list.remove(3)
    print("List after removing element:", my_list)

    # Modifying an element in  list
    my_list[2] = 10
    print("List after modifying element:", my_list)

    # Creating a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("\nOriginal dictionary:", my_dict)

    # Adding a key-value pair to the dictionary
    my_dict['d'] = 4
    print("Dictionary after adding key-value pair:", my_dict)

    # Removing a key-value  from the dictionary
    del my_dict['b']
    print("Dictionary after removing key-value pair:", my_dict)

    # Modifying a value in the dictionary
    my_dict['a'] = 5
    print("Dictionary after modifying value:", my_dict)

    # Creating a set
    my_set = {1, 2, 3, 4, 5}
    print("\nOriginal set:", my_set)

    # Adding an element to the set
    my_set.add(6)
    print("Set after adding element:", my_set)

    # Removing an element from the set
    my_set.remove(3)
    print("Set after removing element:", my_set)

main()
