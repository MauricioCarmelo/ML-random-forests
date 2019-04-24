import pandas as pd
import numpy
import math

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

	def __init__(self):
		self.root = None

	def setTarget(self, target):
		self.target = target
		
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

	def entropy(self, dataframe):
		entropy = 0
		e = 0
		n = float(len(dataframe))
		for c in dataframe[self.target].unique():
			x = len(dataframe.loc[dataframe[self.target] == c])
			e = -(x/n)*(math.log((x/n), 2))
			entropy = entropy + e
		return entropy

	def valueEntropy(self, subframe):
		entropy = 0
		e = 0
		n = float(len(subframe))
		for c in subframe[self.target].unique():
			x = len(subframe.loc[subframe[self.target] == c])
			e = -(x/n)*(math.log((x/n), 2))
			entropy = entropy + e
		return entropy

	def informationGain(self, dataframe):
		entropy = self.entropy(dataframe)
		infoGain = {}
		for attribute in dataframe.columns.values:
			gain = 0
			n = float(len(dataframe))
			for value in dataframe[attribute].unique():
				subframe = dataframe.loc[dataframe[attribute] == value]
				x = len(subframe)
				gain = gain + (x/n) * self.valueEntropy(subframe)

			infoGain[attribute] = entropy - gain
		return infoGain

	def ID3(self, dataframe):
		gains = self.informationGain(dataframe)
		return max(gains, key=gains.get)

	def buildTree(self):

		best_attribute = self.ID3(self.dataframe)
		self.root = Node(best_attribute)
		subframes_d, directions = self.splitDataframe(self.root.getValue(), self.dataframe)

		for attribute_value, subframe in subframes_d.items():
			self.root.insertChild(attribute_value, None)
			self.root.printNode()
			self.buildTreeRecursively(self.root.childs[attribute_value], subframe)
			self.root.printNode()

	def buildTreeRecursively(self, cur_node, dataframe):
	
		best_attribute = self.ID3(dataframe)
		cur_node.setValue(best_attribute)

		## condicoes de parada para a funcao recursiva

		subframes_d, directions = self.splitDataframe(cur_node.getValue(), dataframe)

		## condicoes de parada para a funcao recursiva

		for attribute_value, subframe in subframes_d.items():

			cur_node.insertChild(attribute_value, None)
			self.buildTreeRecursively(cur_node.childs[attribute_value], subframe)