# Move helper functions
FRONT = 1
BACK = 3
LEFT = 2
RIGHT = 4
UP = 5
DOWN = 6

# facelets on the face being rotated
# indices of the arrays
# represent facelet numbers
# clockwise - 90
def cw(facelet):
    f =  [1, 3, 0, 2]
    return f[facelet]
# counter clockwise -90
def ccw(facelet):
    f = [2, 0, 3, 1]
    return f[facelet]
# half turn 180
def half(facelet):
    f = [3, 2, 1, 0]
    return f[facelet]

# Side facelet transitions
# G - clockwise
# Gprime - counterclockwise
# G2 - 180
# face -face number
def upG(face):
    return (face%4)+1
def upGprime(face):
    return ((face+2) % 4) + 1
def upG2(face):
    return ((face+1) % 4) + 1

def downG(face):
    return upG2(face)
def downGprime(face):
    return upG(face)
def downG2(face):
    return upG2(face)

def rightG(face):
    if face == FRONT:
        return UP
    elif face == UP:
        return BACK
    elif face == BACK:
        return DOWN:
    elif face == DOWN:
        return FRONT

def rightGprime(face):
    if face == FRONT:
        return DOWN
    elif face == UP:
        return FRONT
    elif face == BACK:
        return UP:
    elif face == DOWN:
        return BACK

def rightG2(face):
    if face == FRONT:
        return BACK
    elif face == UP:
        return DOWN
    elif face == BACK:
        return FRONT:
    elif face == DOWN:
        return UP

def leftG(face):
    return rightGprime(face)
def leftGprime(face):
    return rightG(face)
def leftG2(face):
    return rightG2(face)

def frontG(face):
    if face == LEFT:
        return UP
    elif face == UP:
        return RIGHT
    elif face == RIGHT:
        return DOWN:
    elif face == DOWN:
        return LEFT

def frontGprime(face):
    if face == LEFT:
        return DOWN
    elif face == UP:
        return LEFT
    elif face == RIGHT:
        return UP:
    elif face == DOWN:
        return RIGHT

def frontG2(face):
    if face == LEFT:
        return RIGHT
    elif face == RIGHT:
        return LEFT:
    elif face == UP:
        return DOWN
    elif face == DOWN:
        return UP
# back is the opposite of front
def backG(face):
    return frontGprime(face)
def backGprime(face):
    return frontG(face)
def backG2(face):
    return frontG2(face)