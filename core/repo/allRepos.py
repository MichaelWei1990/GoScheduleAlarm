from allRoutes import RoutesRepo
from allStops import StopsRepo

class AllRepos:
    __stops_repo = None
    __routes_repo = None

    def __init__(self):
        self.__stops_repo = StopsRepo()
        self.__routes_repo = RoutesRepo()

    def get_stops_repo(self):
        return self.__stops_repo

    def get_routes_repo(self):
        return self.__routes_repo
