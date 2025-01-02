
def matrix_multiply(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

# Test case
A = [[5, 4, 3], [2, 4, 6], [4, 7, 9]]
B = [[3, 2, 4], [4, 3, 6], [2, 7, 5]]
print("Matrix multiplication result:", matrix_multiply(A, B))
