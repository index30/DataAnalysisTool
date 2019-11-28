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
        
    def test_mk_img_tree(self):
        tree_result = self.ic.mk_img_tree()
        print(tree_result)
        self.assertEqual(len(tree_result), 2)
        
    def test_rec_random_pick_imgs(self):
        imgs_dict = self.ic.rec_random_pick_imgs()
        self.assertEqual(len(imgs_dict), 2)
        self.assertCountEqual(list(imgs_dict.keys()), self.ic.mk_img_tree())
        
        


if __name__ == "__main__":
    unittest.main()