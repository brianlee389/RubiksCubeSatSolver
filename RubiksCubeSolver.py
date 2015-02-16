# 2 x 2 Rubiks Cube Solver using Minisat
# This converts how to solve the Rubiks Cube into a Satisfiability Problem
# Minisat will solve the steps needed to solve the cube.
import os
import subprocess
STARTSTATE = 0
NUMFACE = 6
NUMCOLORS = 6
NUMFACELETS = 4
RED = [0, 1, 1]
FRONT = 1
BACK = 2
LEFT = 3
RIGHT = 4
UP = 5
DOWN = 6

#
class MinisatRubiks:
	def __init__(self):
		self.variables = 8
		self.clauses = [[1, 2, 3,4,5,6,7,8],[1],[-2]]
		self.variablemapping = []

	def createSatFile(self):
		numclauses = len(self.clauses)
		f = open('satrubiks.in', 'w')
		f.write('p cnf ')
		f.write(str(self.variables) + ' ')
		f.write(str(numclauses) + '\n')
		for cl in self.clauses:
			for v in cl:
				f.write(str(v) + ' ')
			f.write('0\n')

	def callMinisat(self):
		subprocess.call(["minisat", "satrubiks.in", "satrubiks.out"])

	def parseMinisat(self):
		f = open('satrubiks.out', 'r')
		hi = f.readline()
		print "Variables"
		raw = f.read()
		vars = str.split(raw,' ')
		print vars
h = MinisatRubiks()
h.createSatFile()
h.callMinisat()
h.parseMinisat()
