from Forest import *

class Simulation:
    def __init__(self, folds, parameters):
        self.folds = folds
        self.parameters = parameters

        self.forest_and_test_fold = []          # list of tuples with forest and testing fold
        self.tested_forests = []

#    def get_forests_and_test_folds_t(self):
#        return self.forests_and_test_folds_t

    def train(self):

        k = len(self.folds) - 1
        while k >= 0:
            training_set = pd.DataFrame()
            test_set = pd.DataFrame()
            for i, fold in enumerate(self.folds):       # determine the training and test set
                if i == k:
                    test_set = fold
                else:
                    training_set = training_set.append(fold)

            forest = Forest(training_set, self.parameters)
            forest.train_forest()
            self.forest_and_test_fold.append((forest, test_set))
            k -= 1
        return 0

    def test(self):

        for t in self.forest_and_test_fold:
            forest = t[0]
            test_set = t[1]
            forest.classify(test_set)
            forest.calculate_metrics()
            self.tested_forests.append(forest)
        return 0

    def run(self):
        self.train()
        self.test()
