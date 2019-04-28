from tree import *

def print_tree(node):
    if node.is_leaf():
        print "classe: " + str(node.value)
    else:
        print "node with attribute: " + str(node.value)
        for direction, child in node.childs.items():
            print "going to direction: " + str(direction)
            print_tree(child)

tree = Tree()
tree.load_data_frame("data/input_data3.csv")

tree.set_target("buys_computer")

categoricals = ["age", "income", "student", "credit_rating"]
numerics = []
tree.set_categorical_attributes(categoricals)
tree.set_numerical_attributes(numerics)

raiz = tree.build_tree()

print_tree(raiz)
print
print
inst = {
    "age": "youth",
    "income": "high",
    "student": "no",
    "credit_rating": "fair"
}

print tree.classify(inst, raiz)

