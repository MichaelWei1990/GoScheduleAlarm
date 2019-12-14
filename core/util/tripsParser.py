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
from stopTimesParser import make_trips_from_stop_times_file

from trip import Trip

TRIPS_FILE_ROUTE_ID = 0
TRIPS_FILE_TRIP_ID = 1

def set_route_data(trip_line_date, routes_repo, trip):
    route = routes_repo.get_route_by_id(trip_line_date[TRIPS_FILE_ROUTE_ID])
    route.add_stops(trip.get_stop_ids());
    #stop_times = trips_stop_times_dict[trip_line_date[TRIPS_FILE_TRIP_ID]]
    #set_route_stops(route, trip.get_stop_ids())
    print("Trip data -- Route ID: " + trip_line_date[TRIPS_FILE_ROUTE_ID] + ", Trip ID: " + trip_line_date[TRIPS_FILE_TRIP_ID])

def load_trips(routes_repo, stops_repo, all_trips):
    file = open(trips_file)
    file.readline()    # skip title line
    lines = file.readlines()
    for line in lines:
        trip_data = get_route_and_trip_id_from_line(line)
        set_route_data(trip_data, routes_repo, all_trips[trip_data[TRIPS_FILE_TRIP_ID]])
        
    file.close()

def trim_trip_id_extra_data(trip_id):
    trip_id = trip_id[trip_id.index('-')+1:]
    return trip_id

def test_loading():
    # step 1: create and initialize repos instance
    all_repos = AllRepos()

    # step 2: load the trips-stop-time data
    all_trips = make_trips_from_stop_times_file()

    # load trips
    load_trips(all_repos.get_routes_repo(), all_repos.get_stops_repo(), all_trips)

test_loading()

