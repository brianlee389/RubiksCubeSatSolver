from helper import *

def generate_state_solved_clause_list():
    """
    clauses for whether state m is solved
    """
    minisat_clauses = []
    aggregator = []
    for m in xrange(env.state_variable_min, env.state_variable_max+1):
        for i in xrange(0, 6):
            for j in xrange(0, 4):
                for k in xrange(0, 3):
                    temp = generate_equal_clause_list(l('c', m, i, j, k), env.c_map(i, k))
                    aggregator.append([-1*l('s', m)] + temp[0])
                    aggregator.append([-1*l('s', m)] + temp[1])
        minisat_clauses.append(aggregator)
        aggregator = []
    return minisat_clauses


def generate_atleast_one_clause_list():
    """ 
    creates the atleast one clauses 
    """
    aggregator = []
    for counter in xrange(env.state_variable_min
                          ,env.state_variable_max+1):
        aggregator.append(counter)
    
    return aggregator


def generate_atmost_one_clause_list():
    """ 
    creates the atmost one clauses 
    """
    aggregator = []
    minisat_clauses = []
    for i in xrange(env.state_variable_min
                          ,env.state_variable_max+1):
        for j in xrange(i+1,env.state_variable_max+1):
            aggregator.append([-1*i,-1*j])
        minisat_clauses.append(aggregator)

    return minisat_clauses
