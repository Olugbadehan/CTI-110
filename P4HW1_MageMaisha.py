#Maisha Mage
#11/29/2025
#P4HW1
#Use loops to Calculate average score


#Ask user for number of scores
num_scores = int(input("How many scores do you want to ener? "))

#List for valid scores
score_list = []

#Loop to collect scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    #Validate score
    while not (0 <= score <= 100):
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    #Add valid score to list
    score_list.append(score)

lowest = min(score_list)
#create modified list without the lowest score
modified_list = score_list.copy()
modified_list.remove(lowest)

#Calculate average
average = sum(modified_list) / len(modified_list)

if average >= 90:
    grade = "A"
else:
    if average >= 80:
        grade = "B"
    else:
        if average >= 70:
            grade  = "C"
        else:
            if average >= 60:
                grade = "D"
            else:
                grade = "F"


#Output
print("\n-------------Results--------------")
print(f"{'Lowest Score:':<15}{lowest}")
print(f"{'Modified List:':<15}{modified_list}")
print(f"{'Scores Average:':<15}{average:.2f}")
print(f"{'Grade:':<15}{grade}")
print("--------------------------------------")