import pandas as pd
import numpy
import math


class Node:

	def __init__(self, value=None):
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
		self.dataframe = pd.DataFrame()
		self.categorical = []
		self.numeric = []
		self.a_priori_class = ""
		self.num_average = {}

	def set_dataframe(self, dataframe):
		self.dataframe = dataframe

	def set_target(self, target):
		self.target = target

	def set_categorical_attributes(self, categoricals):
		self.categorical = set(categoricals)

	def set_numerical_attributes(self, numerics):
		self.numeric = set(numerics)

	def set_num_averages(self, numerics):
		for attribute in numerics:
			self.num_average[attribute] = self.dataframe[attribute].sum() / float(len(self.dataframe))

	def set_parameters(self, dataframe, target, categoricals, numerics):
		self.set_dataframe(dataframe)
		self.set_target(target)
		self.set_categorical_attributes(categoricals)
		self.set_numerical_attributes(numerics)
		self.a_priori_class = dataframe[self.target].value_counts().argmax()
		self.set_num_averages(numerics)

	def get_root(self):
		return self.root

	def get_dataframe(self):
		return self.dataframe

	def get_cut(self, attribute):
		return self.num_average[attribute]

	def is_categorical(self, attribute):
		return attribute in self.categorical

	def is_numeric(self, attribute):
		return attribute in self.numeric

	def load_data_frame(self, filepath):
		self.filepath = filepath
		self.dataframe = pd.read_csv(self.filepath)

	def split_data_frame(self, attribute, dataframe):
		d = {}
		if attribute == None:	# if attribute is qualitative #
			print "Attribute is not defined"

		if self.is_categorical(attribute):
			values = dataframe[attribute].unique()
			for value in values:
				subset = dataframe.loc[dataframe[attribute] == value]
				d[value] = subset
			return d, values

		elif self.is_numeric(attribute):
			average = self.get_cut(attribute)
			values = ['left', 'right']

			subset = dataframe.loc[dataframe[attribute] <= average]
			if not subset.empty:
				d['left'] = subset
			subset2 = dataframe.loc[dataframe[attribute] > average]
			if not subset2.empty:
				d['right'] = subset2
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
			gain = 0
			n = float(len(dataframe))
			if self.is_categorical(attribute):

				for value in dataframe[attribute].unique():
					subframe = dataframe.loc[dataframe[attribute] == value]
					x = len(subframe)
					gain = gain + (x/n) * self.value_entropy(subframe)
					infoGain[attribute] = entropy - gain

			elif self.is_numeric(attribute):		# handle numerical attributes
				subframe1 = dataframe.loc[dataframe[attribute] <= self.get_cut(attribute)]
				subframe2 = dataframe.loc[dataframe[attribute] > self.get_cut(attribute)]

				x1 = len(subframe1)
				x2 = len(subframe2)

				gain = gain + (x1/n) * self.value_entropy(subframe1)
				gain = gain + (x2/n) * self.value_entropy(subframe2)
				infoGain[attribute] = entropy - gain

		return infoGain

	def id3(self, dataframe):
		gains = self.information_gain(dataframe)
		return max(gains, key=gains.get)

	def has_only_one_direction(self, dataframe, attribute):	# whether or not there is only one value within the column
		if self.is_categorical(attribute):
			if len(dataframe[attribute].unique()) == 1:
				return True

		elif self.is_numeric(attribute):
			if (len(dataframe.loc[dataframe[attribute] <= self.get_cut(attribute)]) == len(dataframe)) or \
					(len(dataframe.loc[dataframe[attribute] > self.get_cut(attribute)]) == len(dataframe)):
				return True

		return False

	def has_only_one_class(self, dataframe):
		if len(dataframe[self.target].unique()) == 1:
			return True
		return False

	def build_tree(self):
		best_attribute = self.id3(self.dataframe)
		self.root = Node(best_attribute)
		subframes_d, directions = self.split_data_frame(best_attribute, self.dataframe)

		for attribute_value, subframe in subframes_d.items():

			if self.has_only_one_class(subframe):
				resultado = subframe[self.target].unique()
				resultado = resultado[0]
				self.root.childs[attribute_value] = Node(str(resultado))

			#elif self.has_only_one_direction(subframe, best_attribute):		# won't be able to split - infinite loop
			#	return str(subframe[self.target].value_counts().argmax())

			else:
				self.root.childs[attribute_value] = Node()
				self.root.childs[attribute_value].set_value(
					self.build_tree_recursively(self.root.childs[attribute_value], subframe))

		return self.root

	def build_tree_recursively(self, cur_node, dataframe):
		#if len(dataframe[self.target].unique()) == 1:

		if self.has_only_one_class(dataframe):
			resultado = dataframe[self.target].unique()
			resultado = resultado[0]
			return str(resultado)

		best_attribute = self.id3(dataframe)							#cur_node.setValue(best_attribute)

		if self.has_only_one_direction(dataframe, best_attribute): 		# won't be able to split - infinite loop
			return str(dataframe[self.target].value_counts().argmax())

		subframes_d, directions = self.split_data_frame(best_attribute, dataframe)
		for attribute_value, subframe in subframes_d.items():
			cur_node.childs[attribute_value] = Node()
			cur_node.childs[attribute_value].set_value(
				self.build_tree_recursively(cur_node.childs[attribute_value], subframe))
		return best_attribute

	def get_numeric_direction(self, attribute, value):
		if value <= self.get_cut(attribute):
			return 'left'
		else:
			return 'right'

	def classify_instance(self, instance, cur_node):
		if cur_node.is_leaf():
			return cur_node.value
		attribute = cur_node.value

		if self.is_categorical(attribute):
			direction = instance[attribute]

		else:
			direction = self.get_numeric_direction(attribute, instance[attribute])

		if not direction in cur_node.childs:
			return self.a_priori_class
		next_node = cur_node.childs[direction]
		return self.classify_instance(instance, next_node)

	def classify(self, instance):
		return self.classify_instance(instance, self.root)
