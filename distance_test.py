# Messing around with data distances.

from math import sqrt
from random import randint

gridBG = "-"
gridsize = 20

class MakeGrid(object):
    def __init__(self, size):
        self.size = size
        self.grid = {}
        for x in range(size):
            for y in range(size):
                self.grid[y,x] = gridBG

    def printgrid(self):
        print ""
        for x in range(self.size):
            for y in range(self.size):
                print "".join(str(self.grid[y,x])),
                if y == self.size - 1:
                    print "\n",
                    
class DataGuy(object):
    def __init__(self, gender, age, height, weight):
        if gender.lower() == "m":
            self.gender = 1
        elif gender.lower() == "f":
            self.gender = 0
        self.age = age
        self.height = height
        self.weight = weight
    
data = {
    1:DataGuy("m", 23, 101, 135),
    2:DataGuy("m", 25, 121, 202),
    3:DataGuy("m", 66, 33, 222),
    4:DataGuy("f", 11, 11, 145),
}

def dataavg(var):
    """Returns the average of a named DataGuy variable."""
    avg = 0.0
    getdata = "avg += data[i]." + var
    for i in data:
        exec getdata
    return avg / len(data)
    
def datasd(var):
    """Returns the SD of a named DataGuy variable."""
    sd = 0
    getdata = "sd = (data[i]." + var + " - dataavg(var)) ** 2"
    for i in data:
        exec getdata
    return sqrt(sd)
    
def dataminmax(var):
    varlist = []
    getdata = "varlist.append(data[i]." + var + ")"
    for i in data:
        exec getdata
    return min(varlist), max(varlist)

my_vars = ["height", "age"]
for var in my_vars:
    varavg = dataavg(var)
    varsd = datasd(var)
    varmin, varmax = dataminmax(var)
    
def varnorm(var):
    
    ((var - varmin(var)) / (varmax(var) - varmin(var))) * (gridsize - 1)
    
for i in range(len(my_vars)):
    var = "var = data[i]." + i
    exec var
    varnorm(var)

def gridnorm(val, grid):
    pass
    

my_grid = MakeGrid(gridsize)
for i in data:
    my_grid.grid[data[i].height, data[i].age] = "*"

my_grid.grid[2,2] = "X"
print data[1].gender, data[1].age
my_grid.printgrid()

