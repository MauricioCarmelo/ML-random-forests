from Bagging import *
from tree import *


class Forest:

    def __init__(self, dataframe, parameters):
        self.dataset = dataframe    # corresponds to a fold
        self.n_tree = parameters[0]
        self.target = parameters[1]
        self.categorical = parameters[2]
        self.numeric = parameters[3]

        self.bagging = Bagging(self.dataset, self.n_tree)

        self.trees = []
        self.tree_roots = []
        self.tt_tuples = []  # list of tuples of trees and the corresponding instances that will be used for testing

    def get_trees(self):
        return self.tree_roots

    def get_tree_roots(self):
        return self.tree_roots

    def get_test_tuples(self):
        return self.tt_tuples

    def train_forest(self):
        self.bagging.generate_bootstraps()
        bootstraps = self.bagging.get_bootstraps()
        for bootstrap in bootstraps:            # train a tree for each bootstrap
            tree = Tree()
            tree.set_parameters(bootstrap.get_training_set(), self.target, self.categorical, self.numeric)
            tree.build_tree()

            self.trees.append(tree)
            self.tree_roots.append(tree.get_root())
            t = (tree, bootstrap.get_test_set())    # tuple
            self.tt_tuples.append(t)
        return self.trees
