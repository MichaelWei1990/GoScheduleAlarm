from model.stop import Stop
import time

class Target:

    __stop = None
    __arrival_time = None

    def __init__(self, stop, arrival_time):
        __stop = stop
        __arrival_time = arrival_time

    def get_stop(self):
        return self.__stop

    def get_arrival_time(self):
        return self.__arrival_time
    
