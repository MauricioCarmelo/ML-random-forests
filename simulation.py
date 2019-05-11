from Forest import *

class Simulation:

    def __init__(self, folds, parameters):
        self.folds = folds
        self.parameters = parameters

        self.forests_and_test_folds_t = []            # list of tuples with forest and testing fold

    def get_forests_and_test_folds_t(self):
        return self.forests_and_test_folds_t

    def train(self):
        for test_index in range(0, len(self.folds)):
            for i, fold in enumerate(self.folds):        # train the forests
                if i != test_index:
                    forests = []
                    forest = Forest(fold, self.parameters)
                    forests.append(forest)
            t = (forests, self.folds[test_index])
            self.forests_and_test_folds_t.append(t)

    def test(self):

        for t in self.forests_and_test_folds_t:
            forest = t[0]
            test_set = t[1]
            forest.classify(test_set)


        return 0

    def run(self):
        """
            SEPARAR UM FOLD PARA TESTE
            TREINAR FLORESTAS COM OS OUTROS FOLDS
            CLASSIFICAR OS VALORES (COMO?)
        """
        self.train()
        self.test()
