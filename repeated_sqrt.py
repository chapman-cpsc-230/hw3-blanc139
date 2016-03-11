from math import sqrt
for n in range(1, 60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2

    print r

# The program takes any real number between 1 & ,
# takes the square root, squares it again,
# and puts out the same number that was entered.
# However, I don't think I am getting the correct outcome...
