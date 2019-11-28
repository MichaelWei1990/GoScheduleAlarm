from datetime import datetime, timedelta
class Alarm:

    __time = None
    __ringing = False

    def __init__(self, time):
        self.__time = time

    def go_off(self, current_time):
        delta = (self.__time - current_time)
        return (delta.days == -1 or delta.seconds == 0)

    def display_time(self):
        print(self.__time)


alarm = Alarm(datetime(2019,11,27,18,20))
alarm.display_time()

current_time = datetime(2019,11,27,18,20,1)
result = alarm.go_off(current_time)
print(result)