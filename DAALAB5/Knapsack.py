"""
Name: Raunak Thanawala
Experiment: Fractional Knapsack
Batch: C
Registration Number: 231070051
"""
import pandas as pd


def read_csv(filepath):
    data = pd.read_csv(filepath)
    if data.empty:
        raise ValueError("EMPTY FILE")
    if data.isnull().any().any():
        raise ValueError("INVALID SIZE OF COLUMNS")
    for col in data.columns[2:]:
        if not data[col].apply(lambda x: isinstance(x, int) and x > 0).all():
            raise ValueError("INVALID INPUT")
    return data.to_dict(orient='records')


def knapsack(items, capacity):
    for item in items:
        item['value_index'] = item['Cost'] / (item['ShelfLife'] * item['Capacity'])
    items = sorted(items, key=lambda x: x['value_index'], reverse=True)
    total_cost = 0
    current_capacity = 0
    for item in items:
        if current_capacity >= capacity:
            break
        if item['Capacity'] + current_capacity <= capacity:
            total_cost += item['Cost']
            current_capacity += item['Capacity']
        else:
            fraction = (capacity - current_capacity) / item['Capacity']
            total_cost += fraction * item['Cost']
            current_capacity = capacity
    return total_cost


def main():
    filepath = "C:/Users/ASUS/Desktop/Coding/DAA/DAA LAB5/knapsack_data_5.csv"
    capacity = 200
    items = read_csv(filepath)
    cost = knapsack(items, capacity)
    cost = round(cost, 2)
    print(
        f"The Maximum Cost in Transport vehicles such that Items have Max Cost, "
        f"Min Capacity and Min Shelf Life is {cost}"
    )


if __name__ == '__main__':
    main()
