import pandas as pd
import random


class Bootstrap:

    def __init__(self):
        self.training_set = pd.DataFrame()
        self.test_set = pd.DataFrame()

    def get_training_set(self):
        return self.training_set

    def get_test_set(self):
        return self.test_set

    def generate(self, dataframe):
        length = len(dataframe)
        training_indexes = [0] * length

        for i in range(0, length):
            r_number = random.randint(0, length-1)
            training_indexes[r_number] += 1

        print training_indexes
        for idx, item in enumerate(training_indexes):
            if item:
                for i in range(item):
                    self.training_set = self.training_set.append((dataframe.iloc[idx, :]), ignore_index=True)

            else:
                self.test_set = self.test_set.append(dataframe.iloc[idx, :], ignore_index=True)