def split_list(input_list):

    if not input_list:
        return [[], []]

    mid_index = (len(input_list) + 1) // 2

    first_part = input_list[:mid_index]
    second_part = input_list[mid_index:]

    return [first_part, second_part]

print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
