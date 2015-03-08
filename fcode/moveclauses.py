import time
from random import shuffle
from helper import *


#top-x rotation plane mappings
#for f, f', b, b', 2F, 2B
vi_top_x = [1,4,3,5]
#F  => go clockwise
#F' => go anti-clockwise
vj_front = [(3,1),(2,3),(0,2),(1,0)]
#B  => go ant-clockwise
#B' => go clockwise
vj_back  = [(2,0),(0,1),(1,3),(3,2)]

#top-y rotation plane mappings
#for r, r', l, l', l2, r2
vi_top_y = [0,4,3,5]
#R  => go clockwise
#R' => go anti-clockwise
vj_right = [(3,1),(3,1),(0,2),(3,1)]
#L  => go anti-clockwise
#L' => go clockwise
vj_left  = [(2,0),(2,0),(1,3),(2,0)]

#top-z rotation plane mappings
#for u, u', d, d', u2, d2
vi_side_z = [0,1,2,3]
#U  => go clockwise
#U' => go anti-clockwise
vj_up = [(0,1),(0,1),(0,1),(0,1)]
#D  => go anti-clockwise
#D' => go clockwise
vj_down  = [(2,3),(2,3),(2,3),(2,3)]
#unchanged face
unchanged_face = [0,1,3,2]

#shift has value either 1 or 3
# 1 => anticlockwise
# 3 => clockwise

CW = 3
ACW = 1

def fi_u(i, shift):
    # print "fi for ", i
    # print vi_side_z[i]
    # print vi_side_z[( (i+3) % 4 )]
    return vi_side_z[( (i+shift) % 4 )]
    
def fj_u(i, j, shift):
    # print "fj for ", i, j
    # print vj_up[( i % 4 )]
    # print vj_up[( (i+3) % 4 )]
    index = tuple.index(vj_up[( i % 4 )], j)
    return vj_up[( (i+shift) % 4 )][index]

def rotate(i, j, shift):
    shift = (1 if shift == 3 else 3)
    index = list.index(unchanged_face, j)
    return unchanged_face[(index+shift)%4]

"""generate clauses in CNF form of p = q"""
def equal_clauses_list( p, q):
    return [ [p, (-1*q)], [(-1*p), q] ]

def move_U():
    rotation = ACW
    move = "U'"
    minisat_clauses = []
    temp = []

    #the changed part clauses
    for m in xrange(1, 2):
        aggregate = []
        #the 1,2,3,4 faces
        for i in xrange(0,3+1):
            for j in xrange(0,1+1):
                for k in xrange(0,2+1):
                    temp = equal_clauses_list( lu('c',m, i,j,k),lu('c',m-1
                                                                   ,fi_u(i, rotation)
                                                                   ,fj_u(i,j, rotation),k) )
                    [ elem.insert(0, -1*lu(move,m)) for elem in temp ]
                    aggregate = aggregate + temp
            
        #the 5th face
        for j in xrange(0,3+1):
            for k in xrange(0,2+1):
                temp = equal_clauses_list( lu('c',m, 5-1,j,k),lu('c',m-1, 5-1
                                                                 ,rotate(5-1,j, rotation),k) )
                [ i.insert(0, -1*lu(move,m)) for i in temp ]
                aggregate = aggregate + temp 
                    
        minisat_clauses = minisat_clauses + aggregate

    return minisat_clauses

def move_u():
    minisat_clauses = []
    temp = []

    #the unchanged part clauses
    for m in xrange(1, 2):
        aggregate = []
        #the 6th face
        for j in xrange(0,3+1):
            for k in xrange(0,2+1):
                temp = equal_clauses_list( lu('c',m, 6-1,j,k),lu('c',m-1,6-1,j,k) )
                [ elem.insert(0, -1*lu('u',m)) for elem in temp ]
                aggregate = aggregate + temp
                
        #the unchanged facelets
        for i in xrange(0,3+1):
            for j in xrange(2,3+1):
                for k in xrange(0,2+1):
                    temp = equal_clauses_list( lu('c', m, i, j, k),lu('c', m-1, i, j, k) )
                    [ elem.insert(0, -1*lu('u',m)) for elem in temp ]
                    aggregate = aggregate + temp
                    
        minisat_clauses = minisat_clauses + aggregate

    return minisat_clauses


#generate the exactly one moveset clauses
def exactly_one_move_set():
    aggregator = []
    temp = []
    for m in xrange(0, 15):
        for z in env.move_set:
            temp = generate_exactly_one_clause_list([lu(z.upper(), m), lu(z.upper() + "'", m), lu('2' + z.upper(), m)])
            [ elem.insert(0, -1*lu(z,m)) for elem in temp ]
            aggregator = aggregator + temp
    return aggregator

#constrain consecutive disjoint moves clauses
def no_two_consecutive_disjoint_moves():
    aggregator = []
    for m in xrange(0,15-1):
        aggregator.append([-1* lu('u', m), -1* lu('d', m+1)])
        aggregator.append([-1* lu('l', m), -1* lu('r', m+1)])
        aggregator.append([-1* lu('f', m), -1* lu('b', m+1)])
    return aggregator


def run():
    move_U()
