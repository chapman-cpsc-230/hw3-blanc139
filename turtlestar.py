import turtle

bob = turtle.Pen()

inputx = raw_input("Enter an odd number of sides: ")
inputx = int(inputx)

inputy = raw_input("Enter side length: ")
inputy = int(inputy)

for n in range(inputx):
    bob.forward(inputy)
    bob.left(180.0-180.0/inputx)

quitt = raw_input("Hit <enter> to quit!")

turtle.bye()
