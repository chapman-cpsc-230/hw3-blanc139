import turtle

bob = turtle.Pen()

input1 = raw_input("Enter the number of sides: ")
input1 = int(input1)
input2 = raw_input("Enter side length: ")
input2 = int(input2)


for i in range(input1):
    bob.forward(input2)
    bob.left(360/input1)

quit = raw_input("Hit <enter> to quit.")

turtle.bye()
