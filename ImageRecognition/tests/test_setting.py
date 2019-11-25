from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import setting

class TestSetting(unittest.TestCase):
    def setUp(self):
        self.set = setting.Setting()
    
    def tearDown(self):
        del self.set
        
    def test_set_logger(self):
        pass


if __name__ == "__main__":
    unittest.main()