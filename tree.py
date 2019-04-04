import pandas as pd
import numpy

class Node:
	def __init__(self, value=None):
		self.value = value
		self.childs = {}

	def getValue(self):
		return self.value

	def isLeaf(self):
		if not self.childs:
			return True
		return False

	def insertChild(self, direction, value):
		self.value = None # Make sure that this node has empty value, as this is not a leaf anymore
		if direction in self.childs:
			print "Direction ->" + str(direction) + "<-is already set in this node"
		else:
			self.childs[direction] = Node(value)
#	tests
	def printNode(self):
		print "Node value: " + str(self.value)
		print "childs"
		for direction, child in self.childs.items():
			print "\tdirection: " + str(direction)
			print "\tvalue: " + str(child.getValue())
		print


class Tree:
	def __init__(self, value):
		self.root = Node(value)

	def getRoot(self):
		return self.root