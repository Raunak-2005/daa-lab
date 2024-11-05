"""
Name: Raunak Thanawala
Experiment: Gross and Net Salaries
Batch: C
Registration Number: 231070051
"""
import pandas as pd

class Salary:
    def __init__(self, input_csv):
        self.input_csv = input_csv
        self.df = pd.read_csv(self.input_csv, delimiter=';')
        if pd.read_csv(self.input_csv, delimiter=';', nrows=1).empty:
            raise ValueError("EMPTY FILE")
        if self.df.isnull().any().any():
            raise ValueError("INVALID SIZE OF COLUMNS")
        if (self.df['Basic Salary'] < 0).any():
            raise ValueError("INVALID INPUT")

    def calculate_gross_salary(self):
        self.df['Gross Salary'] = (
            self.df['Basic Salary'] + 
            self.df['House Rent Allowance'] +  
            self.df['Other Allowances']
        )

    def calculate_net_salary(self):
        self.df['Net Salary'] = (
            self.df['Gross Salary'] - 
            self.df['Income Tax'] - 
            self.df['Provident Fund'] - 
            self.df['Professional Tax']
        )

    def linear_min_max(self):
        net = self.df['Net Salary']
        ids = self.df['Sr.No']
        max_salary = float("-inf")
        min_salary = float('inf')
        max_id = min_id = 0

        for i in range(len(net)):
            if net.iloc[i] < min_salary:
                min_salary = net.iloc[i]
                min_id = ids.iloc[i]
            if net.iloc[i] > max_salary:
                max_salary = net.iloc[i]
                max_id = ids.iloc[i]

        return min_id, max_id

    def recursive_min_max(self, start, end):
        if start == end:
            employee_id = self.df.iloc[start]['Sr.No']
            return employee_id, employee_id

        mid = (start + end) // 2
        min_left_id, max_left_id = self.recursive_min_max(start, mid)
        min_right_id, max_right_id = self.recursive_min_max(mid + 1, end)

        net_min_left = self.df[self.df['Sr.No'] == min_left_id]['Net Salary'].values[0]
        net_min_right = self.df[self.df['Sr.No'] == min_right_id]['Net Salary'].values[0]
        net_max_left = self.df[self.df['Sr.No'] == max_left_id]['Net Salary'].values[0]
        net_max_right = self.df[self.df['Sr.No'] == max_right_id]['Net Salary'].values[0]

        min_id = min_left_id if net_min_left < net_min_right else min_right_id
        max_id = max_left_id if net_max_left > net_max_right else max_right_id

        return min_id, max_id

def main():
    input_csv = 'Salary5.csv'

    try:
        salary_calculator = Salary(input_csv)
        salary_calculator.calculate_gross_salary()
        salary_calculator.calculate_net_salary()

        min_id_linear, max_id_linear = salary_calculator.linear_min_max()
        print("Linear:")
        print(f"ID with Minimum Salary: {min_id_linear}")
        print(f"ID with Maximum Salary: {max_id_linear}")

        min_id_recursive, max_id_recursive = salary_calculator.recursive_min_max(0, len(salary_calculator.df) - 1)
        print("Divide and Conquer:")
        print(f"ID with Minimum Salary: {min_id_recursive}")
        print(f"ID with Maximum Salary: {max_id_recursive}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
