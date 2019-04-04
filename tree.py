import pandas as pd
import numpy

class Node:
	def __init__(self, value):
		self.value = value
		self.childs = {}

	def getValue(self):
		return self.value

	def isLeaf(self):
		if not self.childs:
			return True
		return False

	def insertChild(self, direction, value):
		if direction in self.childs:
			print "Direction ->" + str(direction) + "<- is already set in this node"
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
	"""
	def __init__(self, value):
		self.root = Node(value) """
	def __init__(self, dataframe):
		self.root = None

		#best_attribute = winner()
		
		self.root = Node(best_attribute)
		for subframe in list_of_subframe:
			buildTree(self.root, subframe)

	def getRoot(self):
		return self.root

	def splitDataframe(self, attribute, dataframe):
		d = {}
		# if attribute is qualitative
		values = dataframe[attribute].unique()
		for value in values:
			subset = dataframe.loc[dataframe[attribute] == value]
			d[value] = subset
		return d, values


	def buildTree(self, cur_node, dataframe):
		datagrams, directions = splitDataframe(cur_node.getValue(), dataframe)



