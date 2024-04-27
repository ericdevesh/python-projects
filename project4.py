# Write a python code to add and delete element from a dictionary using functions

def add_element(dictionary, key, value):
    dictionary[key] = value

def delete_element(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        print("Key not found in dictionary")

# Example usage:
my_dict = {"a": 1, "b": 2, "c": 3}
print("Initial dictionary:", my_dict)
add_element(my_dict, "d", 4)
print("Dictionary after adding element:", my_dict)
delete_element(my_dict, "b")
print("Dictionary after deleting element:", my_dict)
