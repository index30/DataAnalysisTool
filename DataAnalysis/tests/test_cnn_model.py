from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import cnn_model

class TestCNNModel(unittest.TestCase):
    def setUp(self):
        self.cnn = cnn_model.CNNModel()
    
    def tearDown(self):
        del self.cnn


if __name__ == "__main__":
    unittest.main()