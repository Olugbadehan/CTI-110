#Maisha Mage
#12/5/25
#P5LAB 
#Using user-defined functions

import random

def disperse_change(change):
    
    change = round(change * 100)
    print(f"Change owed as integer: {change}")

    num_dollars = change // 100

    change = change - (num_dollars * 100)

    num_quarters = change // 25

    change = change - (num_quarters * 25)

    num_dimes = change // 10

    change = change - (num_dimes * 10)

    num_nickels = change // 5

    change = change - (num_nickels * 5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")


    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")



    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")



    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")



    if num_pennies> 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")


def main():
    #Logic goes here
    
    #Generate the amount
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #Create variable to represent money to put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    #Calculate change owed to customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    #Call the disperse_change function
    disperse_change(change)





#Call the main function
main()
