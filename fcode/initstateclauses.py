
# ---Start of Phase 1---
# read from input file the state in the format
# face 1 color starting letter, separated by space
# face 2 color starting letter, separated by space
# face 3 color starting letter, separated by space
# face 4 color starting letter, separated by space
# face 5 color starting letter, separated by space
# face 6 color starting letter, separated by space

# eg.
# B G P O
# G P O P
# Y Y Y Y
# P B B B
# G G O O
# W W W W

# program working:
# map this color to its corresponding number

# ---End of Phase 1---

import itertools

def get1 (num):
    return 1 if (num == 1) else -1


def create_init_state_clauses(cnums):
    """ 
    Initializes 24 * 3 clauses corresponding to the initial state
    """
    aggregator = []
    counter = 0
    for i in xrange(0,6):
        for j in xrange(0,4):
            for k in xrange(0,3):
                number = l('c', 1, i, j, k)
                aggregator.append([ number*get1(env.b_map[cnums[counter]][k]) ])
                
    return aggregator



def run():
    with open('initstate.txt') as f:
        lines = f.read().splitlines()
        characters = [x.split() for x in lines]
        colors = list(itertools.chain.from_iterable(characters))
        cnums = [env.c_map[c] for c in colors]
        clauses = create_init_state_clauses(cnums)
    return clauses
