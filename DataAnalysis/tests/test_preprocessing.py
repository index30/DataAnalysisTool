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
    
    def test_load_feature_list(self):
        pass
    
    def cut_na(self):
        pass
    
    def split_Xy(self):
        pass
    
    def test_pickup_corr_lists(self):
        pass
    
    def test_devide_intfloat(self):
        pass
    
    def test_devide_binary(self):
        pass
    
    def test_val2int(self):
        pass

if __name__ == "__main__":
    unittest.main()