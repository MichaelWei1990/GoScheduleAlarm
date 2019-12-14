def is_to_finalize(sequence):
    return sequence == 1

def get_time_from_string(time_string):
    times = time_string.split(':')
    return times[0],times[1]

import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model")

from stopTime import StopTime

class Trip:

    __id = ""
    __stop_times = []
    __start = ""
    __destination = ""

    def __init__(self, id):
        self.__id = id
        
    def get_id(self):
        return self.__id

    def add_new_stop(self, id, sequence, depature_time):
        hour, minute = get_time_from_string(depature_time)
        self.__stop_times.append(StopTime(id, hour, minute, ""))
        if is_to_finalize(int(sequence)):
            self.__finalize()
    
    def get_stop_ids(self):
        stop_ids = []
        for stop_time in self.__stop_times:
            stop_ids.append(stop_time.get_stop_id());
        return stop_ids

    def __finalize(self):
        self.__destination = self.__stop_times[0].get_stop_id()
        self.__start = self.__stop_times[-1].get_stop_id()

    
   

