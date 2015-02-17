from random import shuffle
from MoveFunctions import *
import copy

MAXFACELETS = 24
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

CW = 90
CCW = -90
HALF = 180
# Assume (i,j,m,k)
def createCubeFacelet(face,facelet,color=1):
    return (face,facelet,color)

# Assume (i,j,m,k)
def colorFunctionCubeState(c, state):
    f = 'c('+ str(c[0]) + ', ' + str(c[1]) +', ' + str(state) + ', ' + str(c[2]) +')'
    return f

# Assume (i,j,m,k)
def getColor(c):
    return c[2]
def getFacelet(c):
    return c[1]
def getFace(c):
    return c[0]

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
        # index of the color list 
        cind = 0
        # generating face numbers
        for x in range(1,7):
            # generating facelet numbers
            for y in range(0,4):
                # retrieve color:must be between 0-5
                c = colors[cind] % NUMFACE
                b = createCubeFacelet(x,y,c)
                a.append(b)
                # increment color index
                cind = cind + 1
        return a

    # could be abstracted but did it this way to easily understand
    def upMove(self, dir):
        moveface = upG
        movefacelet = cw
        if dir == CCW:
            moveface = upGprime
            movefacelet = ccw
        elif dir == HALF:
            moveface = upG2
            movefacelet = half

        nextStateNum = self.CurrentStateNum + 1
        oldState = copy.deepcopy(self.States[self.CurrentStateNum])
        newState = copy.deepcopy(oldState)
        indexUp = (UP-1)*4
        # UP FACE
        # 0 - retrieve facelet face number
        # 1 - retrieve facelet facelet number
        # 2 - retrieve facelet color
        for j in range(indexUp, indexUp+4):
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(UP, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
        print "-----"
        # Rest of the faces that are changed
        for j in range(0, indexUp):
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))
            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause

    def downMove(self, dir):
        moveface = downG
        movefacelet = cw
        if dir == CCW:
            moveface = downGprime
            movefacelet = ccw
        elif dir == HALF:
            moveface = downG2
            movefacelet = half

        nextStateNum = self.CurrentStateNum + 1
        # create new deep copies of states
        oldState = copy.deepcopy(self.States[self.CurrentStateNum])
        newState = copy.deepcopy(oldState)
        
        indexDown = (DOWN-1)*4
        indexUp = (UP-1)*4

        # DOWN FACE
        for j in range(indexDown, indexDown+4):
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(DOWN, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
        print "-----"
        # Rest of the faces that are changed
        for j in range(0, indexUp):
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))
            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
# back,front, left,right need to account for facelet change
    def frontMove(self, dir):
        moveface = frontG
        movefacelet = cw
        if dir == CCW:
            moveface = frontGprime
            movefacelet = ccw
        elif dir == HALF:
            moveface = frontG2
            movefacelet = half

        nextStateNum = self.CurrentStateNum + 1
        # create new deep copies of states
        oldState = copy.deepcopy(self.States[self.CurrentStateNum])
        newState = copy.deepcopy(oldState)
        
        # index of the front    
        indexFront = (FRONT-1)
        # FRONT FACE
        for j in range(indexFront, indexFront + 4):
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(FRONT, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
        print "-----"
        # Rest of the faces that are changed
        for j in range(indexFront+4, MAXFACELETS):
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))
            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause

    def backMove(self, dir):
        moveface = backG
        movefacelet = cw
        if dir == CCW:
            moveface = backGprime
            movefacelet = ccw
        elif dir == HALF:
            moveface = backG2
            movefacelet = half

        nextStateNum = self.CurrentStateNum + 1
        # create new deep copies of states
        oldState = copy.deepcopy(self.States[self.CurrentStateNum])
        newState = copy.deepcopy(oldState)
        
        # index of the back    
        indexBack = (BACK-1)*4
        # BACK FACE
        for j in range(indexBack, indexBack + 4):
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(BACK, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
        print "-----"
        
        # Rest of the faces that are changed
        rangelist = range(0,indexBack) +range(indexBack+4,MAXFACELETS)
        for j in rangelist:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            # get the state when moved
            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause

    def leftMove(self, dir):
        moveface = leftG
        movefacelet = cw
        if dir == CCW:
            moveface = leftGprime
            movefacelet = ccw
        elif dir == HALF:
            moveface = leftG2
            movefacelet = half

        nextStateNum = self.CurrentStateNum + 1
        # create new deep copies of states
        oldState = copy.deepcopy(self.States[self.CurrentStateNum])
        newState = copy.deepcopy(oldState)
        
        # index of the left    
        indexLeft = (LEFT-1)*4
        # LEFT FACE
        for j in range(indexLeft, indexLeft + 4):
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(LEFT, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
        print "-----"
        
        # Rest of the faces that are changed
        rangelist = range(0,indexLeft) +range(indexLeft+4,MAXFACELETS)
        for j in rangelist:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            # get the state when moved
            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause

    def rightMove(self, dir):
        moveface = rightG
        movefacelet = cw
        if dir == CCW:
            moveface = rightGprime
            movefacelet = ccw
        elif dir == HALF:
            moveface = rightG2
            movefacelet = half

        nextStateNum = self.CurrentStateNum + 1
        # create new deep copies of states
        oldState = copy.deepcopy(self.States[self.CurrentStateNum])
        newState = copy.deepcopy(oldState)
        
        # index of the right    
        indexRight = (RIGHT-1)*4
        # RIGHT FACE
        for j in range(indexRight, indexRight + 4):
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(RIGHT, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause
        print "-----"
        
        # Rest of the faces that are changed
        rangelist = range(0,indexRight) +range(indexRight+4,MAXFACELETS)
        for j in rangelist:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            # get the state when moved
            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))

            # generate the string
            pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
            pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
            print pclause

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

sample.upMove(CCW)
print "---down---"
sample.downMove(CW)
#print states[0]
#for i in range(0,1):
#   print colorFunctionCubeState(sample.States[i][0],i)
