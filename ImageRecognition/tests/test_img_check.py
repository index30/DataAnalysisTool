from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import img_check

class TestImgCheck(unittest.TestCase):
    def setUp(self):
        self.ic = img_check.ImgCheck("sample_data")
    
    def tearDown(self):
        del self.ic
        
    def test_mk_img_list(self):
        other_list = self.ic.mk_img_list("sample_data/other")
        pasta_list = self.ic.mk_img_list("sample_data/pasta")
        self.assertEqual(len(other_list), 8)
        self.assertEqual(len(pasta_list), 8)
        
    def test_mk_img_tree(self):
        tree_result = self.ic.mk_img_tree()
        self.assertEqual(len(tree_result), 2)


if __name__ == "__main__":
    unittest.main()