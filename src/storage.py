import json
import os


class Storage:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if not os.path.exists(self.file_path):
            return {"devices": []}

        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)