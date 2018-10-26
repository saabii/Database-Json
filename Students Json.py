import json
file_name = 'students.txt'
myfile = open(file_name, mode='w', encoding='Latin-1')
base = [
    {'name': 'Sabina', 'surname': 'Muller', 'gender': 'female', 'age': '21'},
    {'name': 'Serega', 'surname': 'Khaletski', 'gender': 'male', 'age': '18'},
    {'name': 'Dmitry', 'surname': 'Kurmyshev', 'gender': 'male', 'age': '24'},
    {'name': 'Anton', 'surname': 'Rayo', 'gender': 'male', 'age': '27'},
    {'name': 'Natasha', 'surname': 'Abelle', 'gender': 'female', 'age': '29'},
    {'name': 'Rares', 'surname': 'Iliescu', 'gender': 'male', 'age': '24'},
    {'name': 'Sabina', 'surname': 'Iliescu', 'gender': 'female', 'age': '21'}
]
json.dump(base, myfile)
myfile.close()

myfile = open(file_name, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

#for user in json_data:
   # print('Name is ' + str(user['name']))
   # print('age is ' + str(user['age']))
class Basa:
    """
    Main class of a DB. It is used for inheritance
    new classes with special type
    """
    def __init__(self, filename, mode='r', encode='utf-8-sig'):
        self.file = open(filename, mode, encoding=encode)

    def request(self):
        try:
            search = input('Enter your request:\n')
        except UnicodeDecodeError:
            print('-=Unicode=-')
        else:
            if search:
                search_list = search.title().split('%')
                try:
                    my_search = dict(map(lambda x: x.split('='), search_list))
                except ValueError:
                    print('Incorrect request')
                else:
                    return my_search

    def close(self):
        self.file.close()