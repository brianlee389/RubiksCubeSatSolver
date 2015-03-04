MAX_M = 15

class environment:
    move_map = { "f":0, "l":1, "b":2, "r":3, "u":4, "d":5
             ,"F":6, "L":7, "B":8, "R":9, "U":10, "D":11
             ,"F'":12, "L'":13, "B'":14, "R'":15, "U'":16, "D'":17
             ,"2F":18, "2L":19, "2B":20, "2R":21, "2U":22, "2D":23 }

    c_map = {  'B': 1
                  ,'P': 2
                  ,'G': 3
                  ,'R': 4
                  ,'Y': 5
                  ,'W': 6
                  }

    b_map = { 1: [0,0,0]
                  ,2: [0,0,1]
                  ,3: [0,1,0]
                  ,4: [0,1,1]
                  ,5: [1,0,0]
                  ,6: [1,0,1]
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
        self.color_variable_min = 1
        self.color_variable_max = (24*max_m*3)
        self.move_variable_min = self.color_variable_max+1
        self.move_variable_max = self.move_variable_min + (24*max_m)
        self.state_variable_min = self.move_variable_max + 1
        self.state_variable_max = self.state_variable_min + max_m

#keeping a generated environment variable
env = environment(MAX_M)

#lookup function for integer map
def l(ch, m, i=0, j=0, k=0):
    """
    color map
    assuming only j is 0 indexed
    """
    if( ch == 'c' ):
        x = m*i*(j+1)*k
        return x if (x <= env.color_variable_max and env.color_variable_min <= x) else None

    """
    state map + move map
    """
    if(ch.lower() == "s"):
        x = env.state_variable_min + m
        return x if ( x < env.state_variable_max + 1 ) else None
    x = env.move_variable_min + env.move_map[ch] + 24*m
    return x if ( x < env.move_variable_max + 1 ) else None

#generate equal clauses
def generate_equal_clause_list( p, q ):
    return [ [p, (-1*q)], [(-1*p), q] ]

#generate exactly one clauses
def generate_exactly_one_clause_list( p, q ):
    return [ [p, q], [(-1*p), (-1*q)] ]



