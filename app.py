from tree import *

"""
tree = Tree("pessoa")
tree.getRoot().insertChild("idade", 25)
tree.getRoot().insertChild("nome", "mauricio")
tree.getRoot().insertChild("altura", 1.85)
tree.getRoot().insertChild("altura", 1.86)
tree.getRoot().printNode()
"""

tree = Tree()
tree.loadDataframe("data/input_data2.csv")
tree.setTarget("prato")
#tree.buildTree()
#print tree.getRoot().getValue()

dataframe = pd.read_csv("data/input_data2.csv")
#tree.informationGain(dataframe)

x = tree.ID3(dataframe)
print x


