import pandas as pd
import numpy

class Node:
	def __init__(self, value=None):
		self.value = value
		self.childs = {}

	def isLeaf(self):
		if not self.childs:
			return True
		return False

	def insertChild(self, direction, value):
		if direction in self.childs:
			print "Direction is already set"
		else:
			self.childs[direction] = Node(value)
#	tests
	def printNode(self):
		print "Node value: " + str(self.value)
		print "childs"
		for direction, child in self.childs:
			print "\tdirection: " + str(direction)
			print "\tvalue" + str(child)
		print


class Tree:
	def __init__(self, value):
		self.root = Node(value)

