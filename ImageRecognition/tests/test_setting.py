from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import setting

class TestSetting(unittest.TestCase):
    def setUp(self):
        self.set = setting.Setting()
        self.logger_file_path = Path(Path.cwd(), "testlog.txt")
    
    def tearDown(self):
        del self.set
        self.logger_file_path.unlink()
        
    def test_set_logger(self):
        test_logger = self.set.set_logger(logger_name=self.logger_file_path.as_posix())
        tl_base_filename = test_logger.handlers[0].baseFilename
        self.assertEqual(tl_base_filename, self.logger_file_path.as_posix())

if __name__ == "__main__":
    unittest.main()