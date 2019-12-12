def is_to_finalize(sequence):
    return sequence == 1

class Trip:

    __id = ""
    __stop_times = []
    __start = ""
    __destination = ""

    def __init__(self, id):
        self.__id = id
        
    def get_id(self):
        return self.__id

    def add_new_stop(self, id, sequence, depature_time):
        self.__stop_times.append((id, depature_time))
        if is_to_finalize(int(sequence)):
            self.__finalize()

    def __finalize(self):
        self.__destination = self.__stop_times[0][0]
        self.__start = self.__stop_times[-1][0]

    
   

