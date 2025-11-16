#Maisha Mage
#11/15/25
#P2HW2
#create a program to calculate grades for modules

#Pseudocode
#Asks the user to enter grades for following modules
#Put all 6 grades into a list 
#Find lowest grade in the list
#Find highest grade in the list
#Find sum of grades in the list
#Compute average = sum of grades /number of grades

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))


grades = [module1, module2, module3, module4, module5, module6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n-------------Results--------------")
print(f"{'Lowest Grade:':<15}{lowest}")
print(f"{'Highest grade:':<15}{highest}")
print(f"{'sum of Grades:':<15}{total}")
print(f"{'Average:':<15}{average:.2f}")
print("--------------------------------------")