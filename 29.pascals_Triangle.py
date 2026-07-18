def generate_row(row):
    ans = 1
    ans_row = [1]

    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        ans_row.append(ans)

    return ans_row


def pascal_triangle(n):
    ans = []

    for i in range(1, n + 1):
        ans.append(generate_row(i))

    return ans


# Example
n = 5
result = pascal_triangle(n)

print(result)