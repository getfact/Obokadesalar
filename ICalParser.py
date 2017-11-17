from SearchData import *
from collections import Counter
import urllib.request

class DataFetcher:
    
    def __init__(self, url, classrooms):
        self.url = url
        self.classrooms = classrooms
        
    def get_name(self):
        pass
        
        
    def get_outputlist(self):

        #Downloading ICAL file.
        response = urllib.request.urlopen(self.url)

        #Parse to utf-8.
        ical_data = response.read()
        ical_package = ical_data.decode('utf-8')

        #Split at start time.
        splitted_ical_package = ical_package.split("DTSTART")

        #Fetching values.
        index = 0
        while index < len(splitted_ical_package) - 1:

            #Gathering elements.
            start_time = splitted_ical_package[index +1][10:14]
            end_time = splitted_ical_package[index +1][34:38]
            location = splitted_ical_package[index +1][171:179]

            #Cleaning string.
            if "S" in location:
                location = location[:-1]

            #Adding to dictionary.
            self.classrooms[location].append(start_time, end_time)
            
        #Formating list.
        for data_list in self.classrooms:
            
            index = 0
            formater = "06:00-"
            while index < len(data_list):
                
                formater += data_list[index] + ", " + data_list[index+1] + "-"
                index += 2
                
            data_list[0] = formater + "21:00"
            del data_list[2]


        
        return self.ical_parsed_list;

df = DataFetcher(novahuset_rooms_url, novahuset_rooms)

print(df.get_outputlist()[1])
