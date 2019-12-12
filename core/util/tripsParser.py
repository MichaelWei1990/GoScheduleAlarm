trip_info_lookup = {"Route_ID":0, "Trip_ID":2}

#trips_file = '/home/michael/PythonProjs/GoScheduleAlarm/resources/GO_GTFS/trips.txt'
trips_file = "/home/michael/PythonProjs/GoScheduleAlarm/core/util/test_trips.txt"

def trim_trip_id_extra_info(trip_id):
    trip_id = trip_id[trip_id.index('-')+1:]
    return trip_id


def get_route_and_trip_id_from_line(line):
    trip_infos = line.split(',')
    trip_id = trim_trip_id_extra_info(trip_infos[trip_info_lookup["Trip_ID"]])
    return (trip_infos[trip_info_lookup["Route_ID"]], trip_id)

def set_route_stops(route, stop_times):
    for stop_time in stop_times:
        route.add_stop(stop_time.get_stop_id())
    route.display_stops()



import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/repo/")
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model/trip/")
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/util/")

from allRepos import AllRepos
from stopTimesParser import StopTimesParser

from trip import Trip

def load_trips(routes_repo, stops_repo, trips_stop_times_dict):
    file = open(trips_file)
    file.readline()    # skip title line
    lines = file.readlines()
    for line in lines:
        trip_data = get_route_and_trip_id_from_line(line)
        route = routes_repo.get_route_by_id(trip_data[0])
        route.display()
        trip_id = trip_data[1]
        stop_times = trips_stop_times_dict[trip_id]
        set_route_stops(route, stop_times)
        print("Trip data -- Route ID: " + trip_data[0] + ", Trip ID: " + trip_data[1])
    file.close()

def trim_trip_id_extra_data(trip_id):
    trip_id = trip_id[trip_id.index('-')+1:]
    return trip_id

def get_trips_stop_times():
    stop_times_file = '/home/michael/PythonProjs/GoScheduleAlarm/resources/GO_GTFS/stop_times.txt'
    # parser = StopTimesParser(stop_times_file)
    # trips_stop_times_dict = {}
    # while(parser.is_loading_finished() == False):
    #     stop_times = parser.get_current_trip_stop_times()
    #     trip_id = trim_trip_id_extra_data(parser.get_current_trip_id())
    #     trips_stop_times_dict[trip_id] = stop_times
    # return trips_stop_times_dict

def test_loading():
    # step 1: create and initialize repos instance
    all_repos = AllRepos()

    # step 2: load the trips-stop-time data
    #trips_stops_times_dict = get_trips_stop_times()

    # load trips
    #load_trips(all_repos.get_routes_repo(), all_repos.get_stops_repo(), trips_stops_times_dict)

test_loading()

