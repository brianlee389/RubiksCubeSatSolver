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

frontIndex = (FRONT-1)
backIndex = (BACK-1)*4
leftIndex = (LEFT-1)*4
rightIndex = (RIGHT-1)*4
upIndex = (UP-1)*4
downIndex = (DOWN-1)*4

frontFacelets = range(frontIndex, frontIndex+4)
backFacelets = range(backIndex, backIndex+4)
rightFacelets = range(rightIndex, rightIndex+4)
leftFacelets = range(leftIndex, leftIndex+4)
upFacelets = range(upIndex, upIndex+4)
downFacelets = range(downIndex, downIndex+4)
        
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
def colorEquals(c,state,c2,state2):
    # returns string c(i,j,m) = c(a,b,c)
    ceq = colorFunctionCubeState(c2, state2)
    ceq = ceq + ' = ' + colorFunctionCubeState(c, state)
    return ceq

# Assume (i,j,m,k)
def getColor(c):
    return c[2]
def getFacelet(c):
    return c[1]
def getFace(c):
    return c[0]

def oppositeFace(face):
    facen = face+1
    if facen == FRONT:
        return BACK
    elif facen == BACK:
        return FRONT
    elif facen == LEFT:
        return RIGHT
    elif facen == RIGHT:
        return LEFT
    elif facen == UP:
        return DOWN
    elif facen == DOWN:
        return UP
    else:
        print "Doesn't work"
        return -1
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
        
        # facelets being changed/unchanged
        unchanged = downFacelets 
        changed = frontFacelets + leftFacelets + backFacelets + rightFacelets
        
        # UP FACE
        # 0 - retrieve facelet face number
        # 1 - retrieve facelet facelet number
        # 2 - retrieve facelet color
        for j in upFacelets:
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            
            # get the state when moved
            ns = createCubeFacelet(UP, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
            print pclause
        print "-----"

        # Rest of the faces that are changed
        for j in changed:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            if getFacelet(facelet) < 2:
                ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))
                # generate the string
                pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
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
        
        # facelets being changed/unchanged
        unchanged = upFacelets 
        changed = frontFacelets + leftFacelets + backFacelets + rightFacelets
        
        # DOWN FACE
        for j in downFacelets:
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
        for j in changed:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)
            if getFacelet(facelet) < 2:
                ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))
                # generate the string
                pclause = colorFunctionCubeState(ns, self.CurrentStateNum+1)
                pclause = pclause + ' = ' + colorFunctionCubeState(oldState[j], self.CurrentStateNum)
                print pclause
# back,front, left,right need to account for facelet change
# TODO
# requires to not go through all the facelets (if statement)
# also which facelets are moved for each turn
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

        # facelets being changed/unchanged
        unchanged = backFacelets
        changed = leftFacelets + rightFacelets + upFacelets + downFacelets

        # FRONT FACE
        for j in frontFacelets:
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(FRONT, movefacelet(fln), getColor(facelet))
            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
            print pclause
        print "-----"

        # Rest of the faces that are changed
        for j in changed:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))
            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
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
        
        # facelets being changed/unchanged
        unchanged = frontFacelets
        changed = leftFacelets + rightFacelets + upFacelets + downFacelets

        # BACK FACE
        for j in backFacelets:
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(BACK, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
            print pclause
        print "-----"
        
        # changed facelets
        for j in changed:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            # get the state when moved
            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
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
        
         # facelets being changed/unchanged
        unchanged = rightFacelets
        changed =  frontFacelets + backFacelets + upFacelets + downFacelets

        # LEFT FACE
        for j in leftFacelets:
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(LEFT, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
            print pclause
        print "-----"
        
        # changed
        for j in rangelist:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            # get the state when moved
            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
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

        # facelets being changed/unchanged
        unchanged = leftFacelets
        changed =  frontFacelets + backFacelets + upFacelets + downFacelets

        # RIGHT FACE
        for j in rightFacelets:
            # facelet state
            facelet = oldState[j]
            fln = getFacelet(facelet) # retrieve facelet number
            # get the state when moved
            ns = createCubeFacelet(RIGHT, movefacelet(fln), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
            print pclause
        print "-----"
        
        for j in changed:
            # facelet state
            facelet = oldState[j]
            facen = getFace(facelet)

            # get the state when moved
            ns = createCubeFacelet(moveface(facen), getFacelet(facelet), getColor(facelet))

            # generate the string
            pclause = colorEquals(oldState[j],self.CurrentStateNum, ns, nextStateNum)
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
