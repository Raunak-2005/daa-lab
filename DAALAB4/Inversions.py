"""
Name: Raunak Thanawala
Experiment: Inversion Counts
Batch: C
Registration Number: 231070051
"""
import pandas as pd


def process_student_course(filepath):
    """Process the student course data from a CSV file."""
    data = pd.read_csv(filepath)
    
    if data.empty:
        raise ValueError("EMPTY FILE")
    
    if data.isnull().any().any():
        raise ValueError("INVALID SIZE OF COLUMNS")
    
    # Validate that all course codes are positive integers
    for col in data.columns[2:]:
        if not data[col].apply(lambda x: isinstance(x, int) and x > 0).all():
            raise ValueError("INVALID INPUT")


def Inversion(filepath):
    """Count the number of inversions in course codes for each student."""
    data = pd.read_csv(filepath)
    count = {0: 0, 1: 0, 2: 0, 3: 0, 'Other': 0}
    
    for index, row in data.iterrows():
        cc = row[2:].values.tolist()
        _, invcount = CountInversions(cc)
        
        # Update the count of inversions
        if invcount in count:
            count[invcount] += 1
        else:
            count['Other'] += 1

    return count


def CountInversions(arr):
    """Recursively count inversions in the array."""
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    L, left_inv = CountInversions(arr[:mid])
    R, right_inv = CountInversions(arr[mid:])
    M, split_inv = MergeAndCountSplit(L, R)
    
    total = left_inv + right_inv + split_inv
    return M, total


def MergeAndCountSplit(arr1, arr2):
    """Merge two sorted arrays and count split inversions."""
    i = j = split_inv = 0
    arr = []
    n = len(arr1) + len(arr2)
    
    for k in range(n):
        if i >= len(arr1):
            arr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            arr.append(arr1[i])
            i += 1
        elif arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
            split_inv += len(arr1) - i

    return arr, split_inv


# Main execution
filepath = "C:/Users/ASUS/Desktop/Coding/DAA/DAA LAB4/student_course_codes_5.csv"
process_student_course(filepath)
result = Inversion(filepath)

# Output the counts of inversions
for invcount, count in result.items():
    print(f"There are {count} students with {invcount} Inversions")
