from collections import defaultdict, namedtuple
import random
import csv

class BuildDictionary:
    def __init__(self, input_file='names.csv'):
        self.input_file = input_file
        self.build_dict = defaultdict(list)
        self.build_tuple = namedtuple('Names', 'year percent sex')
        self._create_dictionary()
    
    def _create_dictionary(self):
        data = open(self.input_file)
        for line in csv.DictReader(data):
            try:
                name = line['name']
                if self.build_dict[name]:
                    year = line['year']
                    self.build_dict[name][0].year.append(year)
                else:
                    name = line['name']
                    sex = line['sex']
                    percent = line['percent']
                    year = line['year']
                    names = self.build_tuple(sex=sex, percent=percent, year=[year])
                    self.build_dict[name].append(names)
            
            except ValueError:
                continue
            
        data.close()
        
    def get_data(self):
        return self.build_dict
    
        
    

