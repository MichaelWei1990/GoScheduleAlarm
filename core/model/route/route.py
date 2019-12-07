class Route:

    __id = ""
    __short_name = ""
    __long_name = ""

    def __init__(self, id, short_name, long_name):
        self.__id = id
        self.__short_name = short_name
        self.__long_name = long_name

    def get_id(self):
        return self.__id
    
    def display(self):
        print("Route ID: " + self.__id + ", short name: " + self.__short_name + ", long name: " + self.__long_name)

    