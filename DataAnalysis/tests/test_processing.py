from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import processing

class TestProcessing(unittest.TestCase):
    def setUp(self):
        params = {"X_train":[],
                  "X_test":[],
                  "y_train":[],
                  "y_test":[]}
        self.p = processing.Processing(params)
    
    def tearDown(self):
        del self.p


if __name__ == "__main__":
    unittest.main()