from helper import *


def test_color_variable_map():
    temp = 0
    #test colors
    for m in xrange(0, env.no_m):
        for i in xrange(0, 6):
            for j in xrange(0, 4):
                for k in xrange(0, 3):
                    temp = lu('c', m, i, j, k)
                    assert( rlu(temp) == (" c(%d, %d, %d, %d)"%(m,i,j,k)) )
    print "* OK *"


def test_move_variable_map():
    temp = 0
    #test move variable map
    for m in xrange(0, env.no_m):
        for move in env.move_set:
            v1 = lu(move, m)
            v2 = lu(move.upper(), m)
            v3 = lu("%s'"%move.upper(), m)
            v4 = lu("2%s"%move.upper(), m)
            
            assert( v1 >= env.move_variable_min  and v1 <= env.move_variable_max )
            assert( v2 >= env.move_variable_min  and v2 <= env.move_variable_max )
            assert( v3 >= env.move_variable_min  and v3 <= env.move_variable_max )
            assert( v4 >= env.move_variable_min  and v4 <= env.move_variable_max )

            assert( rlu(v1) == (" %s%d"%(move,m)) )
            assert( rlu(v2) == (" %s%d"%(move.upper(),m)) )
            assert( rlu(v3) == (" %s'%d"%(move.upper(),m)) )
            assert( rlu(v4) == (" 2%s%d"%(move.upper(),m)) )

    print "* OK *"

#get the list of clauses in which the variable is involved
def obtain_involved_clause_list(input_num, listofclauses):
    aggregator = []
    for clause in listofclauses:
        for num in clause:
            if abs(num) == input_num:
                aggregator.append(clause)
                break
    return aggregator
