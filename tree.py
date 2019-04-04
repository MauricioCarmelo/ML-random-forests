import pandas as pd
import numpy

class Node:
	def __init__(self, name=None):
		self.name = name
		self.childs = {}

	def isLeaf(self):
		if not self.childs:
			return True
		return False

	def insertChild(self, direction, name):
		if direction in self.childs:
			print "Direction is already set"
		else:
			self.childs[direction] = Node(name)



