from Bagging import *
from tree import *
from metrics import *

class Forest:

    def __init__(self, dataframe, parameters):
        self.dataset = dataframe    # corresponds to a fold
        self.n_tree = parameters[0]
        self.target = parameters[1]
        self.positive_result = parameters[2]
        self.categorical = parameters[3]
        self.numeric = parameters[4]

        self.bagging = Bagging(self.dataset, self.n_tree)

        self.trees = []
        self.tree_roots = []
        self.tt_tuples = []  # list of tuples of trees and the corresponding instances that will be used for testing

        self.results = []       # list of tuples with the correct value and the guess decided by all trees via voting
        self.c_matrix = CMatrix(self.positive_result)

    def get_trees(self):
        return self.trees

    def get_tree_roots(self):
        return self.tree_roots

    def get_test_tuples(self):
        return self.tt_tuples

    def get_c_matrix(self):
        return self.c_matrix

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

    def classify(self, test_set):
        for id, instance in test_set.iterrows():
            correct_value = instance[self.target]
            votes = []
            for tree in self.trees:
                vote = tree.classify(instance)
                votes.append(vote)
            r = max(votes, key=votes.count)
            r = r[0]
            self.results.append((correct_value, r))

    def calculate_metrics(self):
        self.c_matrix.populate(self.results)



