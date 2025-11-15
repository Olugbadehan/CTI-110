#Maisha Mage
#11/12/2025
#P2HW1
#The program is going to work exactly as was requested for P1HW2, only the output will be nicely formatted

budget = input("Enter Budget: ")
destination = input("Enter your travel destination: ")
gas = input("How much do you think you will spend on gas?: ")
accomodation = input("Approximately, how much will you need for accomodation/hotel?: ")
food = input("Last, how much do you need for food?: ")

print("------------Travel Expenses------------")
print()

destination = input("Enter your travel destination: ")
budget = float(input("Initial Budget: "))
gas = float(input("Fuel: "))
accomodation = float(input("Accomodation: "))
food = float(input("Food: "))

print("\n------------Travel Expenses------------")
print(f"{'Location:':<15}{destination}")
print(f"{'Initial Budget:':<15}${budget:.2f}")
print(f"{'Fuel:':<15}${gas:.2f}")
print(f"{'Accomodation:':<15}${accomodation:.2f}")
print(f"{'Food:':<15}${food:.2f}")
print("---------------------------------------")


total_expenses = gas + accomodation + food
remaining_balance = budget - total_expenses

print(f"Remaining Balance: ${remaining_balance:.2f}")
