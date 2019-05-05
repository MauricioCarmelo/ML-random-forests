from FileDAO import *
from Bagging import *
from Bootstrap import *
from simulation import *


def print_tree(node):
    if node.is_leaf():
        print "classe: " + str(node.value)
    else:
        print "node with attribute: " + str(node.value)
        for direction, child in node.childs.items():
            print "going to direction: " + str(direction)
            print_tree(child)

filedao = FileDAO()
filedao.load_dataframe("data/input_data3.csv")

target = "buys_computer"
categoricals = ["age", "income", "student", "credit_rating"]
numerics = []
parameters = (5, target, categoricals, numerics)


"""
    SEPARATE THE FOLDS HERE
"""

simulation = Simulation(filedao.get_dataframe(), parameters)    # criar uma simulacao
forest = simulation.run()
roots = forest.get_tree_roots()

print roots

for tree in roots:
    print_tree(tree)
    print
    print


# forests vai receber um dos folds da lista de folds para um valor de K
# para cada fold, criar uma forest

    # forest.create()
    # forest.train()
    # forest.generate_statistics() - nao tenho certeza desse ainda


#bagging = Bagging(3, filedao)
#boots = bagging.generate_bootstraps()

"""
for i, item in enumerate(boots):
    print "Training set " + str(i+1)
    print item.get_training_set()
    print "Test set"
    print item.get_test_set()
    print
"""


