def indexed_names(names_list):
    """
    Replace each value in the given list with its index, followed by a color, space, and the original value.

    Parameters:
    - names_list: List of names.

    Returns:
    - List where each value is replaced by the index, color, space, and the original value.
    """
    return [f"{index}: {name}" for index, name in enumerate(names_list)]

# Test Case 1: List contains only integers
int_list = [1, 2, 3, 4, 5]
result_int = indexed_names(int_list)
print(f"Original List (int): {int_list}")
print(f"Indexed Names (int): {result_int}")
print()

# Test Case 2: List contains integer and float values
mixed_list = [1, 2.5, 3, 4.75, 5]
result_mixed = indexed_names(mixed_list)
print(f"Original List (mixed): {mixed_list}")
print(f"Indexed Names (mixed): {result_mixed}")
print()

# Test Case 3: List contains a combination of integer, string, and float values
mixed_types_list = [1, 'hello', 3.14, 5, 'world']
result_mixed_types = indexed_names(mixed_types_list)
print(f"Original List (mixed types): {mixed_types_list}")
print(f"Indexed Names (mixed types): {result_mixed_types}")
