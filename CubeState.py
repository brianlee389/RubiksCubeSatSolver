from random import shuffle

NUMFACE = 6
NUMCOLORS = 6
NUMFACELETS = 4

def createCubeState(face,facelet,state,color=1):
    return (face, facelet,state,color)

# Assume (i,j,m,k)
def colorFunctionCubeState(c):
    f = 'c('+ str(c[0]) + ',' + str(c[1]) +',' + str(c[2]) +')'

# Assume (i,j,m,k)

#2x2x2 Cube Class
# color order list contains number between 0-25
class RubiksCube:
    # generates for every state for every 
    # face/facelet and assign colors based on colors
    def __init__(self,colors):
        self.states = self.createStates(colors)

    def createStates(self, colors):
        a = []
        if len(colors) != 24:
            print "incorrect colors"
#            return []
        # face number
        for x in range(1,7):
            # facelet
            for y in range(0,4):
                Index = x+y
                c = colors[index] % NUMFACE
                b = createCubeState(x,y,1,c)
                a.append(b)
        return a

colornums = range(1,25)
pcolornums = range(1,25)
shuffle(pcolornums)

sample = RubiksCube(pcolornums)
print sample

for i in range(0,1):
    print colorFunctionCubeState(sample.states[i])
