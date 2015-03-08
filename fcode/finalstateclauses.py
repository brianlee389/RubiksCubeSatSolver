from helper import *

def generate_final_state_clauses():
    aggregator = []
    for i in xrange(0, 6):
        for k in xrange(0, 3):
            aggregator.append(color(i, k))
    return aggregator

    
def run():
    return generate_final_state_clauses()
