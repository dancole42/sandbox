from math import sqrt
from random import randint

class MakeGrid:
    def __init__(self, size):
        self.size = size
        self.grid = {}
        for x in range(size):
            for y in range(size):
                self.grid[y,x] = bgsym # Change this for different blanks.

    def printgrid(self):
        # for i in range(self.size): print i, # Prints X axis. Sucks.
        print ""
        for x in range(self.size):
            for y in range(self.size):
                print "".join(str(self.grid[y,x])),
                if y == self.size - 1:
                    #print str(x) + "\n", # Prints Y axis. Sucks.
                    print "\n",
        

# Abandoned code from when this started as tic-tac-toe.
"""
class Player:
    def __init__(self, name, pos, score = 0):
        self.name = name
        self.score = score
        self.pos = pos

playerone = Player("Dan", "X")
playertwo = Player("Jordana", "O")
"""

# Returns a list of populated grid positions.
def checkV(current_grid, pos):
    check = []
    for i in current_grid:
        if current_grid[i] == pos:
            check.append(i)
    return check

# Calculates the distance between two points.
def dist(p0, p1):
    return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


# Calculates the distances between all points.
def listdist(current_grid, pos):
    distances = []
    for i in range(len(checkV(current_grid, pos))):
        if i == len(checkV(current_grid, pos)) - 1:
            break
        for o in range(len(checkV(current_grid, pos))):
            if o == len(checkV(current_grid, pos)) - 1:
                break
            if o + 1 <> i:
                distances.append(dist(checkV(current_grid, pos)[i], checkV(current_grid, pos)[o + 1]))
    return distances

# Calculates the average distance between all points.
def avgdist(distances):
    d = 0
    for i in distances:
        d += i
    return d / len(distances)

# Have user define grid parameters (size, # of points, and point symbol)
def gridprompts():
    print "Enter grid parameters or hit ENTER for defaults."
    gridsize = int(raw_input("Grid Size >> ") or 45)
    if gridsize > 45: # Limits size to reasonable
        gridsize = 45
    linelen = int(raw_input("Line length >> ") or gridsize * gridsize)
    stars = int(raw_input("Stars to attempt >> ") or gridsize / 2)
    bgsym = raw_input("Background symbol >> ") [:1] or " "
    starsym = raw_input("Star symbol >> ") [:1] or "*"
    pointsym = raw_input("Point Symbol >> ") [:1] or "." # Takes the first input only.
    return gridsize, linelen, stars, bgsym, starsym, pointsym

# Get user paramaters and create the grid
gridsize, linelen, stars, bgsym, starsym, pointsym = gridprompts()
my_grid = MakeGrid(gridsize)

# Populate the grid with points.
# Really mess around here for different lines and stuff.

# Here's where the fun happens! Change the values passed to
# my_grid.grid for all sorts of crazy lines!

for i in range(linelen):
    for l in range(8):
        my_grid.grid[i, gridsize - i/(l+1)] = pointsym
        my_grid.grid[gridsize - i, gridsize - i/(l+1)] = pointsym

# Just for run, random points
for i in range(stars):
    my_grid.grid[randint(0, gridsize), randint(0, gridsize)] = starsym

# Display the grid, points, and average distance.
my_grid.printgrid()
if stars < 1000:
    print "Computing average distance between stars...",
    print avgdist(listdist(my_grid.grid, starsym))
else:
    print """Number of points is too large and since this is just for fun
I don't feel like learing about things like CPU optimization."""
