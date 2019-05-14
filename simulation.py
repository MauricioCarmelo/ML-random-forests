from Forest import *

class Simulation:

    def __init__(self, folds, parameters):
        self.folds = folds
        self.parameters = parameters

        self.forest_and_test_fold = []          # list of tuples with forest and testing fold

    def get_forests_and_test_folds_t(self):
        return self.forests_and_test_folds_t

    def train(self):

        training_set = pd.DataFrame()
        k = len(self.folds) - 1
        for i, fold in enumerate(self.folds):       # determine the training and test set
            if i == k:
                test_set = fold
            else:
                training_set = training_set.append(fold)

        forest = Forest(training_set, self.parameters)
        forest.train_forest()


        return 0

    """
        for test_index in range(0, len(self.folds)):
            for i, fold in enumerate(self.folds):        # train the forests
                if i != test_index:
                    forests = []
                    forest = Forest(fold, self.parameters)
                    forest.train_forest()
                    forests.append(forest)
            t = (forests, self.folds[test_index])
            self.forests_and_test_folds_t.append(t)
    """

    def test(self):

        for t in self.forests_and_test_folds_t:
            forests = t[0]
            test_set = t[1]
            for forest in forests:
                forest.classify(test_set)
                forest.calculate_metrics()

        return 0

    def run(self):

        self.train()
        self.test()

        for t in self.forests_and_test_folds_t:
            forest = t[0]
