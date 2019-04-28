import pandas as pd


class FileDAO:


    def __init__(self):
        self.file_path = ""
        self.data_frame = None

    def load_data_frame(self, file_path):
        self.file_path = filepath
        self.data_frame = pd.read_csv(self.file_path)

    def get_dataframe(self):
        return self.data_frame

