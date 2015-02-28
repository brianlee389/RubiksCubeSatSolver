class environment:
    move_map = { "u":0, "b":1, "l":2, "r":3, "f":4, "d":5
             ,"U":6, "B":7, "L":8, "R":9, "F":10, "D":11
             ,"U'":12, "B'":13, "L'":14, "R'":15, "F'":16, "D'":17
             ,"2U":18, "2B":19, "2L":20, "2R":21, "2F":22, "2D":23 }

    def __str__(self):
        return ("color variable range: ( %d, %d )\n" +
                "move variable range: ( %d, %d )\n"  +
                "state variable range: ( %d, %d )\n") % (self.color_variable_min, self.color_variable_max, self.move_variable_min, self.move_variable_max, self.state_variable_min, self.state_variable_max)        

    def __init__(self, max_m, max_k):
        """
        set the color range c(m, i, j, k) reserved variable count
        assuming i, k start from 1, j starts from 0
        """
        self.color_variable_min = 1
        self.color_variable_max = (24*max_m*max_k)
        self.move_variable_min = self.color_variable_max+1
        self.move_variable_max = self.move_variable_min + (24*max_m)
        self.state_variable_min = self.move_variable_max + 1
        self.state_variable_max = self.state_variable_min + max_m

env = environment(15,3)

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
