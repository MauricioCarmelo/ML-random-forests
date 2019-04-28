import pandas as pd
import numpy
import math


class Node:

	def __init__(self, value = None):
		self.value = value
		self.childs = {}		# Array of nodes

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def is_leaf(self):
		if not self.childs:
			return True
		return False

	def insert_child(self, direction, value):
		if direction in self.childs:
			print "Direction ->" + str(direction) + "<- is already set in this node"
		else:
			self.childs[direction] = Node(value)

	def get_childs(self):
		return self.root.childs


class Tree:

	def __init__(self):
		self.root = None
		self.categorical = []
		self.numeric = []

	def set_target(self, target):
		self.target = target

	def set_categorical_attributes(self, categoricals):
		self.categorical = set(categoricals)

	def set_numerical_attributes(self, numerics):
		self.numeric = set(numerics)

	def is_categorical(self, attribute):
		return attribute in self.categorical

	def is_numeric(self, attribute):
		return attribute in self.numeric
		
	def get_root(self):
		return self.root

	def load_data_frame(self, filepath):
		self.filepath = filepath
		self.dataframe = pd.read_csv(self.filepath)

	def split_data_frame(self, attribute, dataframe):
		d = {}
		if attribute == None:	# if attribute is qualitative #
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

	def value_entropy(self, subframe):
		entropy = 0
		e = 0
		n = float(len(subframe))
		for c in subframe[self.target].unique():
			x = len(subframe.loc[subframe[self.target] == c])
			e = -(x/n)*(math.log((x/n), 2))
			entropy = entropy + e
		return entropy

	def information_gain(self, dataframe):
		entropy = self.entropy(dataframe)
		infoGain = {}
		for attribute in dataframe.columns.values:
			if self.is_categorical(attribute):
				gain = 0
				n = float(len(dataframe))
				for value in dataframe[attribute].unique():
					subframe = dataframe.loc[dataframe[attribute] == value]
					x = len(subframe)
					gain = gain + (x/n) * self.value_entropy(subframe)
					infoGain[attribute] = entropy - gain

			elif self.is_numeric(attribute):		## handle numerical attributes
				print "should not enter here yet"
				#infoGain[attribute] = entropy - gain

		return infoGain

	def id3(self, dataframe):
		gains = self.information_gain(dataframe)
		return max(gains, key=gains.get)

	def build_tree(self):
		best_attribute = self.id3(self.dataframe)
		self.root = Node(best_attribute)
		subframes_d, directions = self.split_data_frame(best_attribute, self.dataframe)

		for attribute_value, subframe in subframes_d.items():
			if len(subframe[self.target].unique()) == 1:
				self.root.childs[attribute_value] = Node(subframe[self.target].unique())

			else:
				self.root.childs[attribute_value] = Node()
				self.root.childs[attribute_value].set_value(
					self.build_tree_recursively(self.root.childs[attribute_value], subframe))

		return self.root

	def build_tree_recursively(self, cur_node, dataframe):
		if len(dataframe[self.target].unique()) == 1:
			return dataframe[self.target].unique()

		best_attribute = self.id3(dataframe)#		cur_node.setValue(best_attribute)
		subframes_d, directions = self.split_data_frame(best_attribute, dataframe)
		for attribute_value, subframe in subframes_d.items():
			cur_node.childs[attribute_value] = Node()
			cur_node.childs[attribute_value].set_value(
				self.build_tree_recursively(cur_node.childs[attribute_value], subframe))
		return best_attribute

	def classify(self):
		return 0