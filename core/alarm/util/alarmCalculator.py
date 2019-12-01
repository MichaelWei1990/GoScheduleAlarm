import datetime
from datetime import datetime as dt
from datetime import timedelta

def calculate_alarm_time(hour, minute, commute_time = timedelta(minutes=20)):
    today = datetime.date.today()
    now = datetime.datetime.now()
    #now = dt(2019,11,28,19,10)  # hard code here to make testing easier
  
    #this function calculates the train's depature time
    def make_depature_time(today, hour, minute, now):
        depature_time = dt(today.year, today.month, today.day, hour, minute)
        delta_time = depature_time - now
        if(delta_time.days == -1):
            depature_time = depature_time + datetime.timedelta(days=1)
        return depature_time

    depature_time = make_depature_time(today, hour, minute, now) - commute_time
    print(depature_time)

calculate_alarm_time(18,10)