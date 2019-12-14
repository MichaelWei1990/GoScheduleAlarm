import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model/route")

from route import Route

train_route_type = 2
route_info_look_up = {"ID": 0, "SHORT_NAME": 2, "LONG_NAME": 3, "TYPE": 4}

def is_train_route(type_str):
    return int(type_str) == train_route_type

def make_route(infos):
    if is_train_route(infos[route_info_look_up["TYPE"]]):
        return Route(infos[route_info_look_up["ID"]], infos[route_info_look_up["SHORT_NAME"]], \
            infos[route_info_look_up["LONG_NAME"]])
    return None


def load_routes(routes_file_name):
    all_routes = {}
    file = open(routes_file_name)
    file.readline()     # skip title line
    lines = file.readlines()
    for line in lines:
        route_infos = line.split(',')
        route = make_route(route_infos)
        if route is None:
            continue
        all_routes[route.get_id()] = route
    file.close()
    return all_routes

# routes_file = '/home/michael/PythonProjs/GoScheduleAlarm/resources/GO_GTFS/routes.txt'
# routes = load_routes(routes_file)
# for route in routes.values():
#     route.display()