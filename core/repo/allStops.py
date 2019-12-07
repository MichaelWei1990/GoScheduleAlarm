import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model")
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/util/")

from stop import Stop
from stopsParser import load_stops

class StopsRepo:

    __all_stops = None

    def __init__(self):
        self.__all_stops = load_stops('/home/michael/PythonProjs/GoScheduleAlarm/core/util/stops.txt')

    def get_stop_by_id(self, id):
        return self.__all_stops.get(id)

    def display_all(self):
        for stop in self.__all_stops.values():
            stop.display()

repo = StopsRepo()
repo.display_all()
