import unittest
from datetime import datetime, timedelta
from alarm import Alarm

date = datetime(2019,11,27)

class TestAlarm(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUp")
        self.alarmtTime = Alarm(datetime(date.year,date.month,date.day,18,20))

    def test_go_off(self):
        print("test_go_off")
        self.assertEqual(self.alarmtTime.go_off(datetime(date.year,date.month,date.day,18,20)), True)
        
        # time: 18:20:01, expect True
        self.assertEqual(self.alarmtTime.go_off(datetime(date.year,date.month,date.day,18,20,1)), True)

        # time: 18:19:59, expect False
        self.assertEqual(self.alarmtTime.go_off(datetime(date.year,date.month,date.day,18,19,59)), False)

    def test_setter_getter(self):
        test_alarm_time = datetime(date.year,date.month,date.day,19,20)
        expected_getter_alarm_time = datetime(date.year,date.month,date.day,19,20)
        self.alarmtTime.set_time(test_alarm_time)
        self.assertEqual(self.alarmtTime.get_time() == expected_getter_alarm_time, True)

if __name__ == '__main__':
    unittest.main()