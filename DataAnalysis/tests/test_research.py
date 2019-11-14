from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import research

class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.res = research.Research()
    
    def tearDown(self):
        del self.res


if __name__ == "__main__":
    unittest.main()