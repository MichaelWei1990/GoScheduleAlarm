import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model")

from stop import Stop
from enum import Enum

StopLookup = {"ID":0, "name": 1, "url": 5}

def load_stops(stopsFile):
    all_stops = {};
    FILE = open(stopsFile)
    FILE.readline()     # skip title line
    lines = FILE.readlines()
    for line in lines:
        def make_stop(line):
            stop_infos = line.split(',')
            return Stop(stop_infos[StopLookup["ID"]], stop_infos[StopLookup["name"]], stop_infos[StopLookup["url"]])
        stop = make_stop(line)
        all_stops[stop.get_id()] = stop; 
    FILE.close()
    return all_stops