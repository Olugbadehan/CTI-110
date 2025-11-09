#Maisha Mage
#11/7/25
#P1HW2
#calculating and displaying budget expenses


budget = input("Enter Budget: ")
destination = input("Enter your travel destination: ")
gas = input("How much do you think you will spend on gas?: ")
accomodation = input("Approximately, how much will you need for accomodation/hotel?: ")
food = input("Last, how much do you need for food?: ")

print("------------Travel Expenses------------")
print()

location = input("Location: ")
budget = int(input("Initial Budget: "))

num1 = int(input("Fuel: "))
num2 = int(input("Accomodation: "))
num3 = int(input("Food: "))

sum_result = num1 + num2 + num3
final_result = budget - sum_result

print("Remaining Balance : ", final_result)

print(budget, "-", num1, "+", num2, "+", num3, "is equal to", final_result, "!!")








