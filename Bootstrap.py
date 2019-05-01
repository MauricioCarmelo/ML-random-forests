import pandas as pd


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

        training_indexes[1] = 2
        training_indexes[2] = 1
        #for i in range(0, length):
            #random = random() Generate ranrom number from 0 to length
            #random = 2
            #training_indexes[random] += 1

        print training_indexes
        for idx, item in enumerate(training_indexes):
            if item:
                for i in range(item):
                    self.training_set = self.training_set.append((dataframe.iloc[idx, :]), ignore_index=True)

            else:
                self.test_set = self.test_set.append(dataframe.iloc[idx, :], ignore_index=True)