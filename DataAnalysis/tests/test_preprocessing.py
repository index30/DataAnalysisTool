from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import preprocessing

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.pp = preprocessing.Preprocessing()
    
    def tearDown(self):
        del self.pp

    def test_load_data(self):
        pass

if __name__ == "__main__":
    unittest.main()