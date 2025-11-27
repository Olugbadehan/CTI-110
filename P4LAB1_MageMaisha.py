#Maisha Mage
#11/26/2025
#P4LAB1
#Use turtle and loops to draw a sqaure and triangle

#Import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#Set turtle options
pen.pensize(5)
pen.pencolor("Green")
pen.shape("arrow")

#code to draw shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)


#While loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

#Wait for user to close window
win.mainloop()

