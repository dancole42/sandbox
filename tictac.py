from math import sqrt

class MakeGrid:
    def __init__(self, size):
        self.size = size
        self.grid = {}
        for x in range(size):
            for y in range(size):
                self.grid[y,x] = "-"

    def printgrid(self):
        for i in range(self.size): print i,
        print ""
        for x in range(self.size):
            for y in range(self.size):
                print "".join(str(self.grid[y,x])),
                if y == self.size - 1:
                    print str(x) + "\n",
        

class Player:
    def __init__(self, name, pos, score = 0):
        self.name = name
        self.score = score
        self.pos = pos

my_grid = MakeGrid(10)
playerone = Player("Dan", "X")
playertwo = Player("Jordana", "O")

my_grid.grid[3,2] = "X"
my_grid.grid[7,2] = "X"
my_grid.grid[2,7] = "X"
my_grid.grid[3,3] = "X"



my_grid.printgrid()

def checkV(current_grid, pos):
    check = []
    for i in current_grid:
        if current_grid[i] == pos:
            check.append(i)
    return check

def dist(p0, p1):
    return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    
def avgdist(current_grid, pos):
    for i in range(len(checkV(current_grid, pos))):
        if i == len(checkV(current_grid, pos)) - 1:
            break
        print dist(checkV(current_grid, pos)[i], checkV(current_grid, pos)[i + 1])
    
avgdist(my_grid.grid, "X")
#print dist(checkV(my_grid.grid))

"""
for i in range(len(checkV(my_grid.grid))):
    ydis = checkV(my_grid.grid)[i][1] - checkV(my_grid.grid)[i - 1][1]
    print xdis
    xdis = checkV(my_grid.grid)[i][0] - checkV(my_grid.grid)[i - 1][0]
    print ydis
"""
#print sqrt(xdis ** 2 + ydis ** 2)
