# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
if name.strip() == "":
    print("Invalid name. Please try again.")
    name = input("Enter customer name: ")

previous = input("Enter previous meter reading: ")
if not previous.isdigit() or int(previous) < 0:
    print("Invalid input. Enter a number 0 or greater.")
    previous = input("Enter previous meter reading: ")
previous = float(previous)

current = input("Enter current meter reading: ")
if not current.isdigit() or int(current) < int(previous):
    print("Invalid input. Current reading must be greater or equal to the previous reading.")
    current = input("Enter current meter reading: ")
current = float(current)

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
