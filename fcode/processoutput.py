from helper import *
output_integers = []
with open('output.txt') as f:
    lines = f.read().splitlines()
    output = lines[1].split()
    output_integers = [int(x) for x in output]

# for i in xrange(0, len(output_integers)):
#     if output_integers[i] > 0:
#         print rlu(i)

#print the state that is true
state_true = 0
for i in xrange(env.state_variable_min, env.state_variable_max+1):
    if output_integers[i] > 0:
        state_true = i

state_true = state_true - env.state_variable_min
print state_true
#print the moves that are true
for i in xrange(env.move_variable_min, env.move_variable_min + ((state_true+1)*24)+1):
    if output_integers[i] > 0:
        print rlu(i)
