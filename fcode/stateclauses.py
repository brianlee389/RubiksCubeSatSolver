# ---Start of Phase 1---
# read from input file the state in the format
# face i color starting letter, separated by space, a newline

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

from helper import *
import itertools

def get1 (num):
    return 1 if (num == 1) else -1

def generate_init_state_clause_list(cnums):
    """ 
    Initializes 24 * 3 clauses corresponding to the initial state
    """
    aggregator = []
    counter = 0
    for i in xrange(0,6):
        for j in xrange(0,4):
            for k in xrange(0,3):
                number = lu('c', 0, i, j, k)
                aggregator.append([ number*get1(env.b_map[cnums[counter]][k]) ])
            counter = counter + 1
    
    return aggregator

def generate_final_state_clause_list():
    aggregator = []
    for i in xrange(0, 6):
        for j in xrange(0,4):
            for k in xrange(0, 3):
                aggregator.append([lu('c', env.no_m-1, i, j, k)])
    return aggregator

def generate_is_mth_state_solved_clause_list():
    """
    clauses for whether state m is solved
    """
    minisat_clauses = []
    aggregator = []
    for m in xrange(0,env.no_m):
        for i in xrange(0, 6):
            for j in xrange(0, 4):
                for k in xrange(0, 3):
                    temp = generate_equal_clause_list(lu('c', m, i, j, k)
                                                      , color(i, k))
                    aggregator.append([-1*lu('s', m)] + temp[0])
                    aggregator.append([-1*lu('s', m)] + temp[1])
        minisat_clauses = minisat_clauses + aggregator
        aggregator = []
    return minisat_clauses


#exactly one state is a solved state
def generate_exactly_one_state_solved_clause_list():
    return generate_exactly_one_clause_list(range(lu('s',0), lu('s',env.no_m-1)+1))

#run the command
def run(inputfilename):
    with open(inputfilename) as f:
        lines = f.read().splitlines()
        characters = [x.split() for x in lines]
        colors = list(itertools.chain.from_iterable(characters))
        cnums = [env.c_map[c] for c in colors]
        init_state_clause_list = generate_init_state_clause_list(cnums)

    for i in init_state_clause_list:
        for j in i:
            print rlu(j)
    # return init_state_clause_list  
    # return init_state_clause_list + \
    #         generate_final_state_clause_list() + \
    #         generate_is_mth_state_solved_clause_list()+ \
    #         generate_exactly_one_state_solved_clause_list()
