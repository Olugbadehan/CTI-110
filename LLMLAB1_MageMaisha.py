#Maisha Mage
#12/4/25
#LLMLAB1
#Use a large language model (e.g., ChatGPT) to generate Python code to generate A quiz game that asks at least 3 questions


# Dan Da Dan Quiz Game
# This program asks 3 questions about the anime Dan Da Dan.
# It gives 1 point for each correct answer and shows the final score.

# Start score at 0
score = 0

print("Welcome to the Dan Da Dan Quiz!")
print("Answer the following questions.\n")

# -------------------------------
# QUESTION 1
# -------------------------------
print("1) What is the name of the high school girl who believes in ghosts but not aliens?")
answer = input("Your answer: ").strip().lower()

# We check if the answer is correct using if and else
if answer == "momo" or answer == "momo ayase":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong. The correct answer is Momo Ayase.\n")

# -------------------------------
# QUESTION 2
# -------------------------------
print("2) What nickname does Momo give to Ken Takakura?")
answer = input("Your answer: ").strip().lower()


if answer == "okarun":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong. The correct answer is Okarun.\n")

# -------------------------------
# QUESTION 3
# -------------------------------
print("3) Dan Da Dan mixes aliens with what kind of supernatural beings?")
print("(Hint: type 'ghosts' or 'spirits')")
answer = input("Your answer: ").strip().lower()


if answer == "ghosts" or answer == "ghost" or answer == "spirits":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong. A big part of the story involves ghosts.\n")

# -------------------------------
# FINAL SCORE RESULTS
# -------------------------------
print("Quiz complete!")
print("You scored", score, "out of 3.\n")

# FINAL MESSAGE 
if score == 3:
    print("Amazing! You are a REAL Dan Da Dan fan!")
else:
    if score == 2:
        print("Nice job! You know Dan Da Dan pretty well.")
    else:
        if score == 1:
            print("You got one right — keep learning!")
        else:
            print("Zero correct. Time to watch Dan Da Dan!")
