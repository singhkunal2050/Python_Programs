#What’s the advantage of using
#a variable here instead of just typing in the number?


import turtle
nbrSides = 6
for steps in range(nbrSides) :
     turtle.right(360/nbrSides)
     for moresteps in range(nbrSides):
         turtle.forward(50)
         turtle.right(360/nbrSides)
