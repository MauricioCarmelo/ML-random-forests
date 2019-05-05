from Bootstrap import *


class Bagging:

    def __init__(self, dataframe, n_tree):
        self.original_dataset = dataframe
        self.bootstraps = []
        self.nTree = n_tree
        #self.generate_bootstraps()

    def load_dataset(self, dataframe):
        self.original_dataset = dataframe
        return self.original_dataset

    def get_bootstraps(self):
        return self.bootstraps

    def generate_bootstraps(self):        # bootstrapping
        for n in range(0, self.nTree):
            b = Bootstrap()
            b.generate(self.original_dataset)
            self.bootstraps.append(b)
        return self.bootstraps
