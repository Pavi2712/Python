def target(numbers, target):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i, j]
            j += 1
        i += 1
    return []
input_list = [2, 7, 11, 15]
target_value = 9
result = target(input_list, target_value)
print("Result:", result)
