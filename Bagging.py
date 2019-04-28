from FileDAO import *
from Bootstrap import *


class Bagging:

    def __init__(self, n_tree):
        self.fileDAO = FileDAO()
        self.fileDAO.load()
        self.nTree = n_tree
        self.original_dataset = None
        self.bootstraps = []

    def load_dataset(self, file_path):
        self.fileDAO = FileDAO()
        self.fileDAO.load(file_path)
        self.original_dataset = self.fileDAO.get_dataframe()

    def generate_bootstraps(self):
        for n in range(0, self.nTree):
            b = Bootstrap(self.original_dataset)
            self.bootstraps.append(b)



