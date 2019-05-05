from Forest import *

class Simulation:

    def __init__(self, fold, parameters):
        self.dataframe = fold
        self.forest = Forest(fold, parameters)

    def run(self):
        self.forest.train_forest()
        return self.forest

    def get_forest(self):
        return self.forest

