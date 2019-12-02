import time

class StopTime:

    __stopID = ""
    __arrivalHour = 0
    __arrivalMinute = 0
    __headSign = ""
    
    def __init__(self, stopID, arrivalHour, arrivalMinute, headSign):
        self.__stopID = stopID
        self.__arrivalHour = arrivalHour
        self.__arrivalMinute = arrivalMinute
        self.__headSign = headSign

    def get_stop_id(self):
        return self.__stopID;

    def get_arrival_time(self):
        return self.__arrivalHour, self.__arrivalMinute

    def get_head_sign(self):
        return self.__headSign

    def __make_time_string(self):
        return str(self.__arrivalHour) + ":" + str(self.__arrivalMinute)

    def display(self):
        print("Stop time -- ID: " + self.__stopID + ", arrival time: " + self.__make_time_string() + ", head sign: " + self.__headSign)


testStopTime = StopTime("UN", 17, 20, "Union Station 17:20 - Lincolnville GO 18:37")
testStopTime.display()