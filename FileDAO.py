import pandas as pd
import math


class FileDAO:


    def __init__(self):
        self.file_path = ""
        self.dataframe = None
        self.folds_d = {}            # dictionary of lists of (len(dataframe)/k)-sized dataframes

    def load_dataframe(self, filepath):
        self.file_path = filepath
        self.dataframe = pd.read_csv(self.file_path)

    def get_dataframe(self):
        return self.dataframe

    def get_folds(self, k):
        if not k in self.folds_d.keys():
            self.generate_list_of_folds(k)
        return self.folds_d[k]

    def generate_list_of_folds(self, k):
        folds = []                  # list of (len(dataframe)/k)-sized dataframes
        length = len(self.dataframe)
        size = int(math.ceil(length/float(k)))
        for i in range(0, k):
            start = i*size
            if start + size > length:
                end = length
            else:
                end = start + size
            folds.append(self.dataframe[start:end])
        self.folds_d[k] = folds

    @staticmethod
    def save_dictionary(prefix, k, n_tree, info_as_dictionary):

        info_as_dataframe = pd.DataFrame(info_as_dictionary)

        filename = prefix + "_" + str(k) + "_" + str(n_tree)
        path = "collected_data/" + filename + ".csv"
        export_csv = info_as_dataframe.to_csv(path, index=None)
