import unittest
from stop import Stop

class TestStop(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUp")
        self.stopMountJoy = Stop("MJ", "Mount Joy GO", "https://www.gotransit.com/en/stations-stops-parking/find-a-station-or-stop/results?stationCode=MJ")


    def test_id(self):
        print("test_id")
        self.assertEqual(self.stopMountJoy.get_id(), "MJ")

    def test_name(self):
        print("test_name")
        self.assertEqual(self.stopMountJoy.get_name(), "Mount Joy GO")

    def test_url(self):
        print("test_url")
        self.assertEqual(self.stopMountJoy.get_url(), "https://www.gotransit.com/en/stations-stops-parking/find-a-station-or-stop/results?stationCode=MJ")
    
if __name__ == '__main__':
    unittest.main()