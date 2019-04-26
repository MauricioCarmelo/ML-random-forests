import pandas as pd
import numpy
import math

class Node:

	def __init__(self, value = None):
		self.value = value
		self.childs = {} # array of nodes

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
		self.categorical = []
		self.numeric = []

	def setTarget(self, target):
		self.target = target

	def setCategoricalAttributes(self, categoricals):
		self.categorical = set(categoricals)

	def setNumericalAttributes(self, numerics):
		self.numeric = set(numerics)

	def isCategorical(self, attribute):
		return attribute in self.categorical

	def isNumeric(self, attribute):
		return attribute in self.numeric
		
	def getRoot(self):
		return self.root

	def loadDataframe(self, filepath):
		self.filepath = filepath
		self.dataframe = pd.read_csv(self.filepath) # open dataframe from CSV file

	def splitDataframe(self, attribute, dataframe):
		d = {}
		# if attribute is qualitative
		if attribute == None:
			print "Attribute is not defined"
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
		#for attribute in self.categorical:
		for attribute in dataframe.columns.values:
			if self.isCategorical(attribute):
				gain = 0
				n = float(len(dataframe))
				for value in dataframe[attribute].unique():
					subframe = dataframe.loc[dataframe[attribute] == value]
					x = len(subframe)
					gain = gain + (x/n) * self.valueEntropy(subframe)
					infoGain[attribute] = entropy - gain
			elif self.isNumeric(attribute):
				## handle numerical attributes
				print "should not enter here yet"
				#infoGain[attribute] = entropy - gain
		return infoGain

	def ID3(self, dataframe):
		gains = self.informationGain(dataframe)
		#print gains
		return max(gains, key=gains.get)

	def buildTree(self):

		best_attribute = self.ID3(self.dataframe)
		#print "Best attribute = " + str(best_attribute)
		self.root = Node(best_attribute)
		subframes_d, directions = self.splitDataframe(best_attribute, self.dataframe)

		for attribute_value, subframe in subframes_d.items():

			# condicao de parada
			if len(subframe[self.target].unique()) == 1:
				self.root.childs[attribute_value] = Node(subframe[self.target].unique())

			else:
				self.root.childs[attribute_value] = Node()
				self.root.childs[attribute_value].setValue(self.buildTreeRecursively(self.root.childs[attribute_value], subframe))

		return self.root

	def buildTreeRecursively(self, cur_node, dataframe):

		# condicao de parada
		if len(dataframe[self.target].unique()) == 1:
			return dataframe[self.target].unique()

		best_attribute = self.ID3(dataframe)#		cur_node.setValue(best_attribute)
		subframes_d, directions = self.splitDataframe(best_attribute, dataframe)

		for attribute_value, subframe in subframes_d.items():
			cur_node.childs[attribute_value] = Node()
			cur_node.childs[attribute_value].setValue(
				self.buildTreeRecursively(cur_node.childs[attribute_value], subframe))
			# condicao de parada para folha
#			if len(subframe[self.target].unique()) == 1:
#				# create a leaf node
#				cur_node.childs[attribute_value].childs[] = Node()
#				cur_node.childs[attribute_value].setValue(subframe[self.target].unique()[0])
				#return subframe[self.target].unique()[0]
#				return best_attribute
#			else:
#				cur_node.childs[attribute_value] = Node()
#				cur_node.childs[attribute_value].setValue(self.buildTreeRecursively(cur_node.childs[attribute_value], subframe))

		return best_attribute


