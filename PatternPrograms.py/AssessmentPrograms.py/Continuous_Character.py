def count_contiguous_characters(char_list):
    result = []
    length = 0
    while length < len(char_list):
        current_char = char_list[length]
        count = 1
        index = length + 1
        while index < len(char_list) and char_list[index] == current_char:
            count += 1
            index += 1
        if current_char != '':
            result.append(str(count) + current_char)
        length = index
    return result
input_list = ['a', 'a', 'b', 'c', 'a', 'd', 'd', 'e', '']
output = count_contiguous_characters(input_list)
print("Result:", output)
