import pandas as pd
import math
from itertools import islice


class FileDAO:


    def __init__(self):
        self.file_path = ""
        self.raw_dataframe = None
        self.dataframe = pd.DataFrame()
        self.folds_d = {}            # dictionary of lists of (len(dataframe)/k)-sized dataframes

    def load_dataframe(self, filepath, types):
        self.file_path = filepath
        self.dataframe = pd.read_csv(self.file_path, dtype=types) # open class as string

    def load_raw_dataframe(self, filepath):
        self.file_path = filepath
        self.raw_dataframe = pd.read_csv(self.file_path)

    def get_dataframe(self):
        return self.dataframe

    def get_folds(self, k):
        if not k in self.folds_d.keys():
            self.generate_list_of_folds(k)
        return self.folds_d[k]

    def assemble_numeric_columns(self, numerics, target):

        cutting_value = {}
        for attribute in numerics:
            sorted_dataframe = self.raw_dataframe.sort_values(by=attribute)
            differences = []

            pre_row = sorted_dataframe.iloc[0]
            for index, cur_row in islice(sorted_dataframe.iterrows(), 1, None):

                if pre_row[target] != cur_row[target]:
                    differences.append((float(cur_row[attribute] + pre_row[attribute]))/2.0)

                pre_row = cur_row

            cutting_value[attribute] = sum(differences) / float(len(differences))

        # build new dataframe
        for index, cur_row in islice(self.raw_dataframe.iterrows(), 0, None):

            columns = self.raw_dataframe.columns.values
            new_row = pd.Series(index = columns)
            for attribute in columns:
                if attribute == target:     # set the class
                    new_row[attribute] = cur_row[attribute]
                else:
                    if cur_row[attribute] <= cutting_value[attribute]:
                        new_row[attribute] = 'left'
                    else:
                        new_row[attribute] = 'right'

            self.dataframe = self.dataframe.append(new_row, ignore_index=True)

        return self.dataframe

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

    def save_converted_dataframe(self, path_and_name):
        #path_and_name = "data/converted_input.csv"
        export_csv = self.dataframe.to_csv(path_and_name, index=None)
        return 0

    @staticmethod
    def save_dictionary(prefix, sufix, k, n_tree, info_as_dictionary):

        info_as_dataframe = pd.DataFrame(info_as_dictionary)

        filename = prefix + "_k_" + str(k) + "_ntree_" + str(n_tree) + sufix
        path = "collected_data/" + filename + ".csv"
        export_csv = info_as_dataframe.to_csv(path, index=None)

