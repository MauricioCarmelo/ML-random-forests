import pandas as pd
import numpy

class Node:
	def __init__(self, value):
		self.value = value
		self.childs = {}

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value = value

	def isLeaf(self):
		if not self.childs:
			return True
		return False

	def insertChild(self, direction, value):
		if direction in self.childs:
			print "Direction ->" + str(direction) + "<- is already set in this node"
		else:
			self.childs[direction] = Node(value)

	def getChilds(self):
		return self.root.childs

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

		best_attribute = self.winner(self.dataframe)
		self.root = Node(best_attribute)
		subframes_d, directions = self.splitDataframe(self.root.getValue(), self.dataframe)

		for attribute_value, subframe in subframes_d.items():
			self.root.insertChild(attribute_value, None)
			self.root.printNode()
			self.buildTreeRecursively(self.root.childs[attribute_value], subframe)
			self.root.printNode()

	def buildTreeRecursively(self, cur_node, dataframe):
	
		best_attribute = winner(dataframe)
		cur_node.setValue(best_attribute)

		## condicoes de parada para a funcao recursiva

		subframes_d, directions = self.splitDataframe(cur_node.getValue(), dataframe)

		## condicoes de parada para a funcao recursiva

		for attribute_value, subframe in subframes_d.items():

			cur_node.insertChild(attribute_value, None)
			self.buildTreeRecursively(cur_node.childs[attribute_value], subframe)

