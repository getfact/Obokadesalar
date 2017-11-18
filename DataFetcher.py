from SearchData import *
import urllib.request
import io

class DataFetcher:
#Constructor.    
    def __init__(self, url, classrooms):
        #Values.
        self.url = url
        self.classrooms = classrooms

#Private functions.
    #Time formater.
    def __format_time(self, time_data):
    
        data = time_data.split("\n")
        formated_data = data[0].split("\r")
        cleaned_data = formated_data[0][9:13]
    
        return cleaned_data[:2] + ":" + cleaned_data[2:4]

    #Parse to io-file.
    def __ical_parsing(self, response):
        
        ical_data = response.read()
        ical_package = ical_data.decode('utf-8')
        file = io.StringIO(ical_package.strip())

        return file

    def __format_output(self):
        #Values.
        output = ""
        #Format to string output.
        for classroom in self.classrooms:
            if len(self.classrooms[classroom]) > 0:
                output += classroom + " : 06:00-"
                index = 0

                while index < len(classroom) - 2:
                    output += self.classrooms[classroom][index] + ", " + self.classrooms[classroom][index+1] + "-"
                    index += 2

                output += "21:00" + "\n"
            else:
                output += classroom + " : Obokad" + "\n"

        return output

    #Extract data from ical package to dictionary.
    def __data_extraction(self, response):
        #Values.
        start_time = ""
        end_time = ""
        location = ""
        
        #Append data to dictionary.
        for line in self.__ical_parsing(response):
            field, _, data = line.partition(':')

            if field in("DTSTART"):
                start_time = self.__format_time(data)
        
            elif field in("DTEND"):
                end_time = self.__format_time(data)

            elif field in ("LOCATION"):
                location_data = data.split("\n")
                cleaned_location = location_data[0].split("\r")

                #If scheduled time has multiple classrooms.
                if " " in cleaned_location[0]:
                    location_list = cleaned_location[0].split(" ")
            
                    for location in location_list:
                        self.classrooms[location].append(start_time)
                        self.classrooms[location].append(end_time)
                
                else:
                    self.classrooms[cleaned_location[0]].append(start_time)
                    self.classrooms[cleaned_location[0]].append(end_time)

#Public functions.
    #Create output from university house.
    def build_output(self):
        #Downloading ICAL file.
        response = urllib.request.urlopen(self.url)

        self.__data_extraction(response)
            
        return self.__format_output()

df = DataFetcher(novahuset_rooms_url, novahuset_rooms)
print(df.build_output())
