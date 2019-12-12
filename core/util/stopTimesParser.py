import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model")
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model/trip")

from stopTime import StopTime
from trip import Trip

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


# item index in line
TRIP_ID = 0
DEPARTURE_TIME = 2
STOP_ID = 3
STOP_SEQUENCE = 4
STOP_HEADSIGN = 7

def read_data_from_line(line):
    items = line.split(',')
    return items[TRIP_ID], items[DEPARTURE_TIME], items[STOP_ID], items[STOP_SEQUENCE]

def is_new_trip(current_trip_id, trip_id_in_line):
    return (not current_trip_id) or (current_trip_id != trip_id_in_line)

def trim_trip_id_extra_data(trip_id):
    return trip_id[trip_id.index('-') + 1:]

def make_new_trip(trip_id):
    return Trip(trip_id)

# def set_trip_data(trip, depature_time_str, stop_id, stop_sequence):


def make_trips_from_stop_times_file():
    file_name = '/home/michael/PythonProjs/GoScheduleAlarm/resources/GO_GTFS/stop_times.txt'
    file = open(file_name)
    file.readline()      # skip title line
    lines = file.readlines()

    current_trip_id = ""
    current_trip = None
    all_trips = {}

    for line in lines:
        trip_id, depature_time_str, stop_id, stop_sequence = read_data_from_line(line)
        if is_new_trip(current_trip_id, trip_id):
            new_trip = make_new_trip(trim_trip_id_extra_data(trip_id))
            all_trips[new_trip.get_id()] = new_trip
            current_trip = new_trip
            current_trip_id = trip_id
        current_trip.add_new_stop(stop_id, stop_sequence, depature_time_str)
    return all_trips

all_trips = make_trips_from_stop_times_file()
        