class Route:

    __id = ""
    __short_name = ""
    __long_name = ""
    __stops = set()

    def __init__(self, id, short_name, long_name):
        self.__id = id
        self.__short_name = short_name
        self.__long_name = long_name

    def get_id(self):
        return self.__id

    def add_stop(self, stop_id):
        self.__stops.add(stop_id)

    def add_stops(self, stop_ids):
        for id in stop_ids:
            self.__stops.add(id)
        self.display_stops()

    def display_stops(self):
        print("Route has below stops:")
        for stop in self.__stops:
            print(stop)

    
    def display(self):
        print("Route ID: " + self.__id + ", short name: " + self.__short_name + ", long name: " + self.__long_name)

    