def second_largest(sample_list):
    first_largest = 0
    second_largest = 0

    for number in sample_list:
        if number > first_largest:
            second_largest = first_largest
            first_largest = number
        elif number > second_largest and number != first_largest:
            second_largest = number

    return second_largest

sample_list_value = [2, 3, 1, 6, 7]
output = second_largest(sample_list_value)
print("Second largest number", output)
