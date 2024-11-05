def matrix_chain_order(dimensions):
    n = len(dimensions) - 1  # number of matrices
    m = [[0] * n for _ in range(n)]  # DP table to store minimum multiplications

    # l is chain length
    for l in range(2, n + 1):  # l = 2 means considering pairs, up to full length
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # Cost of splitting the chain at k
                cost = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]  # minimum cost to multiply from matrix 1 to matrix n

# Example usage
# Input: Dimensions of matrices in the chain
dimensions = []  # Example dimensions for six matrices

result = matrix_chain_order(dimensions)
print(f"Minimum number of multiplications needed: {result}")
