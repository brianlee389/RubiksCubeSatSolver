import time
from random import shuffle
from helper import *


face_map = {"f": [1,4,3,5],
            "b": [4,1,5,3],
            "l": [4,0,5,2],
            "r": [4,2,5,0],
            "u": [0,1,2,3],
            "d": [3,2,1,0],
            }

move_facelet_map = {"f": [(3,1),(2,3),(0,2),(1,0)],
                    "b": [(1,0),(0,2),(2,3),(3,1)],
                    "l": [(0,2),(0,2),(0,2),(3,1)],
                    "r": [(3,1),(0,2),(3,1),(3,1)],
                    "u": [(0,1),(0,1),(0,1),(0,1)],
                    "d": [(2,3),(2,3),(2,3),(2,3)]
                    }

#unchanged face
unchanged_face = [0,1,3,2]

def fi(move_ch, i, shift):
    # print "fi for ", i
    # print vi_side_z[i]
    # print vi_side_z[( (i+3) % 4 )]
    return face_map[move_ch][(i+shift) % 4]
    
def fj(move_ch, i, j, shift):
    # print "fj for ", i, j
    # print vj_up[( i % 4 )]
    # print vj_up[( (i+3) % 4 )]
    return move_facelet_map[move_ch][ (i+shift) % 4 ][j]

def rotate(j, shift):
    if shift != 2:
        shift = (shift + 2) %4
    index = list.index(unchanged_face, j)
    return unchanged_face[(index+shift)%4]

"""generate clauses in CNF form of p = q"""
def equal_clauses_list( p, q):
    return [ [p, (-1*q)], [(-1*p), q] ]

#one per move, 3 per move set
def move_changed(move_ch, rotation):
    move_string = get_move_string(move_ch, rotation)
    minisat_clauses = []
    temp = []

    #the changed part clauses
    for m in xrange(1, env.no_m):
        aggregate = []
        #the slided faces
        for i in xrange(0,4):
            for j in xrange(0,2):
                for k in xrange(0,2+1):
                    temp = equal_clauses_list( lu('c'
                                                  ,m
                                                  ,face_map[move_ch][i]
                                                  ,move_facelet_map[move_ch][i][j],k)
                                               ,lu('c'
                                                   ,m-1
                                                   ,fi(move_ch, i, rotation)
                                                   ,fj(move_ch, i, j, rotation),k) )
                    [ elem.insert(0, -1*lu(move_string,m)) for elem in temp ]
                    aggregate = aggregate + temp

        rotated_face_number = env.move_set.index(move_ch)
        #the rotated face
        for j in xrange(0,3+1):
            for k in xrange(0,2+1):
                temp = equal_clauses_list( lu('c',m, rotated_face_number,j,k)
                                           ,lu('c',m-1, rotated_face_number
                                               , rotate(j, rotation),k) )
                [ i.insert(0, -1*lu(move_string,m)) for i in temp ]
                aggregate = aggregate + temp 
                    
        minisat_clauses = minisat_clauses + aggregate

    return minisat_clauses

#one per move set
def move_unchanged(move_ch):
    minisat_clauses = []
    temp = []

    unchgd_findex = env.opposite_fmap[env.move_set.index(move_ch)]
    opp_move_ch = env.move_set[unchgd_findex]
    #the unchanged part clauses
    for m in xrange(1, env.no_m):
        aggregate = []
        #the opposite unchanged face
        for j in xrange(0,3+1):
            for k in xrange(0,2+1):
                temp = equal_clauses_list( lu('c',m, unchgd_findex,j,k)
                                           ,lu('c',m-1,unchgd_findex,j,k) )
                [ elem.insert(0, -1*lu(move_ch,m)) for elem in temp ]
                aggregate = aggregate + temp

        #the unchanged facelets
        for i in xrange(0,3+1):
            for j in xrange(0,2):
                for k in xrange(0,2+1):
                    temp = equal_clauses_list( lu('c'
                                                  ,m
                                                  ,face_map[opp_move_ch][i]
                                                  ,move_facelet_map[opp_move_ch][i][j],k)
                                                  ,lu('c'
                                                      ,m-1
                                                      ,face_map[opp_move_ch][i]
                                                      ,move_facelet_map[opp_move_ch][i][j],k) )
                    [ elem.insert(0, -1*lu(move_ch,m)) for elem in temp ]
                    aggregate = aggregate + temp
                    
        minisat_clauses = minisat_clauses + aggregate

    return minisat_clauses


#generate the exactly one move from moveset clauses
def exactly_one_move_from_move_set():
    aggregator = []
    temp = []
    for m in xrange(1, env.no_m):
        for z in env.move_set:
            temp = generate_exactly_one_clause_list([lu(z.upper(), m), lu(z.upper() + "'", m), lu('2' + z.upper(), m)])
            [ elem.insert(0, -1*lu(z,m)) for elem in temp ]
            aggregator = aggregator + temp
    return aggregator

#exactly one move set is true
def exactly_one_move_set():
    aggregator = []
    for m in xrange(1, env.no_m):
        aggregator = aggregator + generate_exactly_one_clause_list([lu(z, m) for z in env.move_set])
    return aggregator


#constrain consecutive disjoint moves clauses
def no_two_consecutive_disjoint_moves():
    aggregator = []
    for m in xrange(1,env.no_m-1):
        aggregator.append([-1* lu('u', m), -1* lu('d', m+1)])
        aggregator.append([-1* lu('l', m), -1* lu('r', m+1)])
        aggregator.append([-1* lu('f', m), -1* lu('b', m+1)])
    return aggregator


def run():
    aggregator = []
    aggregator = aggregator + exactly_one_move_set()
    aggregator = aggregator + exactly_one_move_from_move_set()

    #the move clauses
    for move in env.move_set:
        aggregator = aggregator + move_unchanged(move)
        aggregator = aggregator + move_changed(move, env.NORMAL)
        aggregator = aggregator + move_changed(move, env.PRIME)
        aggregator = aggregator + move_changed(move, env.DOUBLE)

    aggregator = aggregator + no_two_consecutive_disjoint_moves()

    return aggregator
