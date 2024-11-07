def lcs_multiple(grades):
    def lcs(grade1, grade2):
        m = len(grade1)
        n = len(grade2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grade1[i - 1] == grade2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + grade1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
        
        return dp[m][n]
    
    max_sequence = ""
    g = len(grades) 
    for i in range(g):
        common_sequence = grades[i]

        for j in range(g):
            common_sequence = lcs(common_sequence, grades[j])
            if not common_sequence: 
                break
        max_sequence = max(max_sequence, common_sequence, key=len)
    return max_sequence

sequences = []
for i in range(20):
    s = input(f"Enter Grades of Student {i+1} with spaces in between:\n")
    sequences.append(s.replace(" ",""))
result = lcs_multiple(sequences)
if result == "":
    print("No Longest Common Subsequence")
else:
    print("Longest common subsequence:", result)
