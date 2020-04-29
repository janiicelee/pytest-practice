import json

class StudentDB:
    def __init__(self):
        self.__data = None
    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)
            # loading the json file as dict

    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                print("student")
                return student 
                
    def close(self):
        pass