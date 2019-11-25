import unittest
from stop import Stop

class TestStop(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUp")
        self.stopMountJoy = Stop("MJ", "Mount Joy GO", "https://www.gotransit.com/en/stations-stops-parking/find-a-station-or-stop/results?stationCode=MJ")
        self.stopUnionStation = Stop("UN", "Union Station", "https://www.gotransit.com/en/stations-stops-parking/find-a-station-or-stop/results?stationCode=UN")


    def test_id(self):
        print("test_id")
        self.assertEqual(self.stopMountJoy.get_id(), "MJ")
        self.assertEqual(self.stopUnionStation.get_id(), "UN")

    def test_name(self):
        print("test_name")
        self.assertEqual(self.stopMountJoy.get_name(), "Mount Joy GO")
        self.assertEqual(self.stopUnionStation.get_name(), "Union Station")

    def test_url(self):
        print("test_url")
        self.assertEqual(self.stopMountJoy.get_url(), "https://www.gotransit.com/en/stations-stops-parking/find-a-station-or-stop/results?stationCode=MJ")
        self.assertEqual(self.stopUnionStation.get_url(), "https://www.gotransit.com/en/stations-stops-parking/find-a-station-or-stop/results?stationCode=UN")
    
if __name__ == '__main__':
    unittest.main()