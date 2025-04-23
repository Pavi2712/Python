def swap_case(input_string):
    result = ''

    for char in input_string:
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)
        elif 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += char
    return result
sample_text = "HeLlO wOrlD"
output = swap_case(sample_text)
print(output)
