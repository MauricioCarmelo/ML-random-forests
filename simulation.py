from Forest import *
from FileDAO import *

class Simulation:
    def __init__(self, folds, parameters):
        self.folds = folds
        self.parameters = parameters
        self.k = len(self.folds)
        self.n_tree = parameters[0]

        self.forest_and_test_fold = []          # list of tuples with forest and testing fold
        self.tested_forests = []

        # metrics
        self.accuracy = []
        self.error_rate = []
        self.recall = []
        self.sensibility = []
        self.precision = []
        self.specificity = []
        self.fp_rate = []

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

    def populate_metrics(self):
        for forest in self.tested_forests:
            c_matrix = forest.get_c_matrix()
            self.accuracy.append(c_matrix.get_accuracy())
            self.error_rate.append(c_matrix.get_error_rate())
            self.recall.append(c_matrix.get_recall())
            self.sensibility.append(c_matrix.get_sensibility())
            self.precision.append(c_matrix.get_precision())
            self.specificity.append(c_matrix.get_specificity())
            self.fp_rate.append(c_matrix.get_fp_rate())

    def save(self):

        # save the results of each forest
        for i, forest in enumerate(self.tested_forests):
            prefix = "forestresult_" + str(i)
            results = forest.get_results()
            info = {
                "results": results
            }
            FileDAO.save_dictionary(prefix, self.k, self.n_tree, info)

        # save metrics
        metrics = {
            "accuracy": self.accuracy,
            "error_rate": self.error_rate,
            "recall": self.recall,
            "sensibility": self.sensibility,
            "precision": self.precision,
            "specificity": self.specificity,
            "fp_rate": self.fp_rate
        }
        FileDAO.save_dictionary("simulationmetrics", self.k, self.n_tree, metrics)

    def run(self):
        self.train()
        self.test()
        self.populate_metrics()
        self.save()
