import random
import csv

# Updated header with additional columns
header = [
    "Sr.No", 
    "Basic Salary", 
    "House Rent Allowance", 
    "Other Allowances", 
    "Income Tax", 
    "Provident Fund", 
    "Professional Tax"
]

data = []

for i in range(1, 2001):
    serial_number = i
    basic_salary = int(random.uniform(30000, 70000))
    house_rent_allowance = int(random.uniform(5000, 10000))
    other_allowances = int(random.uniform(2000, 4000))
    income_tax = int(0.3 * basic_salary)
    provident_fund = int(random.uniform(1000, 5000))
    professional_tax = int(random.uniform(100, 500))
    
    # Constructing each row with the new format
    row = [
        serial_number, 
        basic_salary, 
        house_rent_allowance, 
        other_allowances, 
        income_tax, 
        provident_fund, 
        professional_tax
    ]
    data.append(row)

# Updated filename and delimiter to use semicolons
filename = "Salary4.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(header)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully with semicolon-separated values.")
