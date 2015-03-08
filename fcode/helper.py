class environment:
    move_set = ["f", "l", "b", "r", "u", "d"]
    
    move_map = { "f":0, "l":1, "b":2, "r":3, "u":4, "d":5
                 ,"F":6, "L":7, "B":8, "R":9, "U":10, "D":11
                 ,"F'":12, "L'":13, "B'":14, "R'":15, "U'":16, "D'":17
                 ,"2F":18, "2L":19, "2B":20, "2R":21, "2U":22, "2D":23 }

    rmove_map = dict((v, k) for k, v in move_map.iteritems())
    
    c_map = {  'R': 1
               ,'B': 2
               ,'P': 3
               ,'G': 4
               ,'Y': 5
               ,'W': 6
               }

    b_map = { 0: [0,0,0]
              ,1: [1,0,0]
              ,2: [0,1,0]
              ,3: [1,1,0]
              ,4: [0,0,1]
              ,5: [1,0,1]
              }

    def __str__(self):
        return ("color variable range: ( %d, %d )\n" +
                "move variable range: ( %d, %d )\n"  +
                "state variable range: ( %d, %d )\n") % (self.color_variable_min
                                                         , self.color_variable_max
                                                         , self.move_variable_min
                                                         , self.move_variable_max
                                                         , self.state_variable_min
                                                         , self.state_variable_max)        

    def __init__(self, max_m):
        """
         set the color range c(m, i, j, k) reserved variable count
        assuming i, k start from 1, j starts from 0
        """
        self.color_variable_min = 0
        self.color_variable_max = (max_m*6*4*3)-1
        self.move_variable_min = self.color_variable_max +1
        self.move_variable_max = self.move_variable_min + (24*max_m) -1
        self.state_variable_min = self.move_variable_max + 1
        self.state_variable_max = self.state_variable_min + max_m-1

#keeping a generated environment variable
env = environment(15)

def assert_limits(i,j,k):
    assert(i < 6 and i >= 0), i
    assert(j < 4 and j >= 0), j
    assert(k < 3 and k >= 0), k

#lookup the final state color bit
def color(i, k):
    return lu('c', 14, i, 0, k)
    
#lookup function for integer map
def lu(ch, m, i=0, j=0, k=0):
    """
    color map
    assuming all m, i, j, k are 0 indexed
    """
    assert( m < 15 and m >= 0 )
    if( ch == 'c' ):
        assert_limits(i,j,k)
        state = m*6*4*3
        face = i*4*3
        facelet = j*3
        x = state + face + facelet + k
        return x if (x <= env.color_variable_max and env.color_variable_min <= x) else None

    """
    state map + move map
    """
    if(ch.lower() == "s"):
        x = env.state_variable_min + m
        return x
    x = env.move_variable_min + env.move_map[ch] + 24*m
    return x

#reverse lookup (integer->character)
def rlu(number):
    return_string = " "
    if( number < 0):
        return_string = "!"
        number = -number
        
    if number >= env.color_variable_min and number <= env.color_variable_max:
        m = number/(6*4*3)
        number = number % (6*4*3)
        i = number/(4*3)
        number = number %(4*3)
        j = number/3
        number = number%3
        k = number
        return_string = ("%sc(%d, %d, %d, %d)" %(return_string, m, i, j, k))
    elif number >= env.move_variable_min and number <= env.move_variable_max:
        number = number - env.move_variable_min
        m = number/24
        move = number % 24
        return_string = ("%s%s%d") % (return_string, env.rmove_map[move], m)
    elif number >= env.state_variable_min and number <= env.state_variable_max:        
        return_string = "%ss%d" % (return_string, (number - env.state_variable_min))
    else:
        raise ValueError("Can't map value ", number)
    return return_string
        
#generate equal clauses
def generate_equal_clause_list( p, q ):
    return [ [p, (-1*q)], [(-1*p), q] ]

#generate atleast one clause list
def generate_atleast_one_clause_list( listofvariables ):
    return [listofvariables]

#generate atmost one clause list
def generate_atmost_one_clause_list( listofvariables ):
    aggregator = []
    for i in xrange(0, len( listofvariables ) ):
        for j in xrange( i+1, len( listofvariables ) ):
            aggregator.append([-1*listofvariables[i], -1*listofvariables[j]])
    return aggregator

#generate exactly one clauses
def generate_exactly_one_clause_list( listofvariables ):
    return generate_atleast_one_clause_list(listofvariables) + generate_atmost_one_clause_list(listofvariables)

def print_clause_list(clause_list):
    aggregator = []
    for clause in clause_list:
        for variable in clause:
            aggregator.append(rlu(variable))
        print " v ".join(aggregator)
        aggregator = []
