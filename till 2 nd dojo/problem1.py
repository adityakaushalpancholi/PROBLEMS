"""
Problem: Electricity bill calculation using slab-based pricing.

Write a program that repeatedly accepts electricity consumption values from the user,
calculates the bill for each input, and continues until the user enters a negative
number or types 'exit' to stop.

The billing structure is based on tiered slab rates:
- 0 to 50 units: 3.50 per unit
- 51 to 100 units: 4.00 per unit
- 101 to 200 units: 5.50 per unit
- 201 to 300 units: 6.50 per unit
- Above 300 units: 7.50 per unit

For each valid input, the program should display the corresponding total bill.
"""


def calculate_bill(units):
    """Return the total electricity bill for a given number of units."""
    if units <= 0:
        return 0.0

    slabs = [
        (50, 3.50),
        (100, 4.00),
        (200, 5.50),
        (300, 6.50),
        (float('inf'), 7.50),
    ]

    bill = 0.0
    start = 0

    for limit, rate in slabs:
        if units <= start:
            break

        end = min(units, limit)
        if end > start:
            bill += (end - start) * rate
        start = end

    return bill


while True:
    user_input = input("Enter electricity consumption in units (negative number or 'exit' to stop): ")
    command = user_input.strip().lower()

    if command == 'exit':
        print("Program terminated.")
        break

    try:
        units = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")
        continue

    if units < 0:
        print("Negative value entered. Exiting program.")
        break

    total_bill = calculate_bill(units)
    print(f"Units consumed: {units:.2f}")
    print(f"Total bill: Rs. {total_bill:.2f}")
    print()
