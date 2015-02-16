from random import shuffle

NUMFACE = 6
NUMCOLORS = 6
NUMFACELETS = 4
RED = [0, 1, 1]

FRONT = 1
BACK = 3
LEFT = 2
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

#2x2x2 Cube Class
# color order list contains number between 0-25
class RubiksCube:
    # generates for every state for every 
    # face/facelet and assign colors based on colors
    def __init__(self,colors):
        state =  self.createState(colors)
        self.States = []
        self.CurrentStateNum = 0
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
    
    def upMove():
        nextStateNum = self.CurrentStateNum + 1
        newState = copy.deepcopy(self.States[self.CurrentStateNum])
        indexUp = (UP-1)*4
        for u in range(indexUP, indexUP+4):
            createCubeFacelet(UP, newState[1], newState)
            #StatenewState[u]

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
