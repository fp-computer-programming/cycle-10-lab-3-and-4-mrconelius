def double_stuff(input_list):
    """
    Double each value in the given list, regardless of its type.

    Parameters:
    - input_list: List of values to be doubled.

    Returns:
    - List with each value doubled.
    """
    return [value * 2 for value in input_list]

# Test Case 1: List contains only integers
int_list = [1, 2, 3, 4, 5]
result_int = double_stuff(int_list)
print(f"Original List (int): {int_list}")
print(f"Doubled List (int): {result_int}")
print()

# Test Case 2: List contains integer and float values
mixed_list = [1, 2.5, 3, 4.75, 5]
result_mixed = double_stuff(mixed_list)
print(f"Original List (mixed): {mixed_list}")
print(f"Doubled List (mixed): {result_mixed}")
print()

# Test Case 3: List contains a combination of integer, string, and float values
mixed_types_list = [1, 'hello', 3.14, 5, 'world']
result_mixed_types = double_stuff(mixed_types_list)
print(f"Original List (mixed types): {mixed_types_list}")
print(f"Doubled List (mixed types): {result_mixed_types}")
