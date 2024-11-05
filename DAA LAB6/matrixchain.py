def get_matrix_dimensions():
    matrices = []
    print("Enter Dimensions of Temperature Matrix")
    trow = int(input("Rows: "))
    tcol = int(input("Columns: "))
    matrices.append((trow, tcol))

    print("Enter Dimensions of Dew Point Matrix")
    trow = int(input("Rows: "))
    tcol = int(input("Columns: "))
    matrices.append((trow, tcol))

    print("Enter Dimensions of Wind Direction Matrix")
    trow = int(input("Rows: "))
    tcol = int(input("Columns: "))
    matrices.append((trow, tcol))

    print("Enter Dimensions of Wind Speed Matrix")
    trow = int(input("Rows: "))
    tcol = int(input("Columns: "))
    matrices.append((trow, tcol))

    print("Enter Dimensions of Cloud Cover Matrix")
    trow = int(input("Rows: "))
    tcol = int(input("Columns: "))
    matrices.append((trow, tcol))

    print("Enter Dimensions of Cloud Layer Matrix")
    trow = int(input("Rows: "))
    tcol = int(input("Columns: "))
    matrices.append((trow, tcol))

    sorted_matrices = sort_matrices_for_multiplication(matrices)
    if sorted_matrices is None:
        print("Cannot arrange matrices for multiplication.")
        return None

    # Build the dimensions array for matrix chain order
    dimensions = [sorted_matrices[0][0]]  # Start with the first matrix's row count
    dimensions.extend(matrix[1] for matrix in sorted_matrices)  # Add each matrix's column count
    return dimensions

def sort_matrices_for_multiplication(matrices):
    # Sort matrices to make them compatible for multiplication
    n = len(matrices)
    sorted_matrices = [matrices[0]]
    used = [False] * n
    used[0] = True

    for _ in range(n - 1):
        found = False
        for i in range(1, n):
            if not used[i]:
                # Check if we can append this matrix to the current chain
                if sorted_matrices[-1][1] == matrices[i][0]:
                    sorted_matrices.append(matrices[i])
                    used[i] = True
                    found = True
                    break
                # Check if we can prepend this matrix to the current chain
                elif matrices[i][1] == sorted_matrices[0][0]:
                    sorted_matrices.insert(0, matrices[i])
                    used[i] = True
                    found = True
                    break
        if not found:
            return None  # If we cannot find a compatible matrix, return None

    return sorted_matrices

# Matrix Chain Multiplication function
def matrix_chain_order(dimensions):
    n = len(dimensions) - 1
    m = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]

# Main code to run the program
dimensions = get_matrix_dimensions()
if dimensions:
    result = matrix_chain_order(dimensions)
    print(f"Minimum number of multiplications needed: {result}")
