from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import img_check

class TestImgCheck(unittest.TestCase):
    def setUp(self):
        self.ic = img_check.ImgCheck("sample_data")
        self.img_suffix = ['jpg', 'JPG', 'png']
    
    def tearDown(self):
        del self.ic
        
    def test_mk_img_tree(self):
        tree_result = self.ic.mk_img_tree()
        self.assertEqual(len(tree_result), 2)
        
    def test_rec_random_pick_imgs(self):
        imgs_dict = self.ic.rec_random_pick_imgs()
        # Check this method can pick up from directory which has image
        self.assertEqual(len(imgs_dict), len(self.ic.mk_img_tree()))
        for img_key in imgs_dict.keys():
            # Check this method can pick without not image suffix 
            self.assertIn(Path(img_key).suffix[1:], self.img_suffix)
        
    def test_rec_random_pick_annotations(self):
        # TODO: Set annotations
        pass


if __name__ == "__main__":
    unittest.main()