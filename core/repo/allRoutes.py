import os
import sys
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/model/route")
sys.path.append("/home/michael/PythonProjs/GoScheduleAlarm/core/util/")

from route import Route
from routeParser import load_routes

class RoutesRepo:

    __all_routes = None

    def __init__(self):
        self.__all_routes = load_routes('/home/michael/PythonProjs/GoScheduleAlarm/resources/GO_GTFS/routes.txt')

    def get_route_by_id(self, id):
        return self.__all_routes.get(id)

    def display_all(self):
        for route in self.__all_routes.values():
            route.display()


repo = RoutesRepo()
repo.display_all()
