import unittest
from trip import Trip

class TestTrip(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        print("setUp")
        self.tripST7726 = Trip("20191205-ST-7726", "ST - Lincolnville GO")
        

    def test_id(self):
        print("test_id")
        self.assertEqual(self.tripST7726.get_id(), "20191205-ST-7726")

    def test_head_sign(self):
        print("test_head_sign")
        self.assertEqual(self.tripST7726.get_head_sign(), "ST - Lincolnville GO")

if __name__ == '__main__':
    unittest.main()