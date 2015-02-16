from random import shuffle

STARTSTATE = 0
NUMFACE = 6
NUMCOLORS = 6
NUMFACELETS = 4
RED = [0, 1, 1]
FRONT = 1
BACK = 2
LEFT = 3
RIGHT = 4
UP = 5
DOWN = 6

# Assume (i,j,m,k)
def createCubeFacelet(face,facelet,color=1):
    return (face,facelet,color)

# Assume (i,j,m,k)
def colorFunctionCubeState(c, state):
    f = 'c('+ str(c[0]) + ',' + str(c[1]) +',' + str(state) +')'
    return f

# Assume (i,j,m,k)
def getColor(c):
    return c[2]

# face transition function for UP
# clockwise - 90
def upf(i):
    if i == 0:
        return 1
    elif i == 1:
        return 3
    elif i == 2:
        return 0
    elif i == 3:
        return 2

def upg(i):
    return (i%4)+1

# counter clockwise -90
def upfprime(i):
    if i == 0:
        return 2
    elif i == 1:
        return 0
    elif i == 2:
        return 3
    elif i == 3:
        return 1

def upgprime(i):
    return ((i+2) % 4) + 1

# half turn 180
def upf2(i):
    if i == 0:
        return 3
    elif i == 1:
        return 2
    elif i == 2:
        return 1
    elif i == 3:
        return 0

def upg2(i):
    return ((i+1) % 4) + 1
# end face transition functions

#2x2x2 Cube Class
# color order list contains number between 0-25
class RubiksCube:
    # generates for every state for every 
    # face/facelet and assign colors based on colors
    def __init__(self,colors):
        state =  self.createState(colors)
        self.States = []
        self.States.append(state)

    def createState(self, colors):
        a = []
        if len(colors) != 24:
            print "incorrect colors"
            return []
        # generating face numbers
        for x in range(1,7):
            # generating facelet numbers
            for y in range(0,4):
                index = 4*(x-1)+y
                c = colors[index] % NUMFACE
                b = createCubeFacelet(x,y,c)
                a.append(b)
        return a
    
    # incompleted
    def moveFunction(self, face, dir):
        sn = len(self.States)
        fn = upf
        gn = upg
        if dir == 1:
            fn = upfprime
            gn = upgprime
        elif dir == 2:
            fn = upf2
            gn = upg2

        #compute function
        # (fn,gn)
    #incompleted
    def createMappings(self):
        return 0

    def getStates(self):
        return self.States

    def addState(self,state):
        self.States.append(state)



# test code
colornums = range(1,25)
pcolornums = range(1,25)
shuffle(pcolornums)
sample = RubiksCube(colornums)
states = sample.getStates()

print states[0]
for i in range(0,1):
    print colorFunctionCubeState(sample.States[i][0],i)
