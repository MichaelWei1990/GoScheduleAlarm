import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model")

from stopTime import StopTime

def get_trip_id_from_line(line):
    return line.split(',')[0]

# def get_stop_id_from_lien(line):
#     return line.split(',')[3]

def get_time_from_string(time_string):
    times = time_string.split(':')
    return times[0],times[1]

def make_stop_time_from_line(line):
    stop_time_infos = line.split(',')
    hour, minute = get_time_from_string(stop_time_infos[1])
    return StopTime(stop_time_infos[3], hour, minute, stop_time_infos[7])

class StopTimesParser:

    __loadingFinished = False
    __loadingFailed = False
    __currentTripID = ""
    __file = None
    __lines = None
    __lines_num = 0
    __currentLineIdx = 0

    def __init__(self, fileName):
        self.__file = open(fileName)
        self.__file.readline()      # skip title line
        self.__lines = self.__file.readlines()
        self.__lines_num = len(self.__lines)
        if(self.__lines_num >  0):
            self.__currentTripID = get_trip_id_from_line(self.__lines[0])

    def get_current_trip_id(self):
        return self.__currentTripID

    def is_loading_finished(self):
        return self.__loadingFinished

    def __get_current_line(self):
        return self.__lines[self.__currentLineIdx]

    def __continue_reading_stops(self):
        if(self.__currentLineIdx >= self.__lines_num):
            self.__loadingFinished = True
            return False          
        return (get_trip_id_from_line(self.__get_current_line()) == self.__currentTripID)

    def get_current_trip_stop_times(self):
        stop_times = []
        while(self.__continue_reading_stops()):
            stop_times.append(make_stop_time_from_line(self.__get_current_line()))
            self.__currentLineIdx = self.__currentLineIdx + 1
        
        if(self.__loadingFinished == False):
            self.__currentTripID = get_trip_id_from_line(self.__get_current_line())
        return stop_times



testStopTimesFile = '/home/michael/PythonProjs/GoScheduleAlarm/core/util/test_stopTimes.txt'      
stopTimeParser = StopTimesParser(testStopTimesFile)
currentTripID = stopTimeParser.get_current_trip_id()
print(currentTripID)

while(stopTimeParser.is_loading_finished() == False):
    stop_times = stopTimeParser.get_current_trip_stop_times()
    for stop in stop_times:
        stop.display()

print("That's all")