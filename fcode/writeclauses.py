import sys
import stateclauses
import moveclauses
from helper import *
from testlookupvariable import *


def main(filename):
    aggregator = []
    aggregator = aggregator + stateclauses.run(filename)
    aggregator = aggregator + moveclauses.run()

    #print_clause_list(aggregator)             
    print "p cnf %d %d" % (env.state_variable_max+1, len(aggregator))
    for clause in aggregator:
        for i in clause:
            z = abs(i)+1
            if abs(i) == env.first_val:
                z = 1
            if i < 0:
                print -1*z,
            else:
                print z,
        print "0"

    # test_color_variable_map()
    # test_move_variable_map()

if __name__ == "__main__":
   main(sys.argv[1])
