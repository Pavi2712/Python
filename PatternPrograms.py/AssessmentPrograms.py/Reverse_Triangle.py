def reverse_triangle(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()
n_value = 5
reverse_triangle(n_value)