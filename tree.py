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

	def __init__(self):
		self.root = None
		
	def getRoot(self):
		return self.root

	def loadDataframe(self, filepath):
		self.filepath = filepath
		self.dataframe = pd.read_csv(self.filepath) # open dataframe from CSV file


	def splitDataframe(self, attribute, dataframe):
		d = {}
		# if attribute is qualitative
		values = dataframe[attribute].unique()
		for value in values:
			subset = dataframe.loc[dataframe[attribute] == value]
			d[value] = subset
		return d, values

	
	def winner(self):
		return "temperatura"

	def buildTree(self):

		best_attribute = self.winner()

		self.root = Node(best_attribute)

		subframes_d, directions = self.splitDataframe(self.root.getValue(), self.dataframe)

		for key, val in subframes_d.items():
			print key
			print val
			print

#		for subframe in list_of_subframe:
#			buildTreeRecursively(self.root, subframe)




	def buildTreeRecursively(self, cur_node, dataframe):
		#datagrams, directions = splitDataframe(cur_node.getValue(), dataframe)
		print "nao estou sendo chamada ainda"


