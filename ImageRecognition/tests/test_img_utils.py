from pathlib import Path
import sys
import unittest

sys.path.append(Path(__file__).resolve().parents[1].as_posix())
import img_utils

class TestImgUtils(unittest.TestCase):
    def setUp(self):
        self.category_list = ["drink", "other", "pasta"]
        self.class_file_path = Path(Path.cwd(), "sample_data/classes.txt")
    
    def tearDown(self):
        pass
        
    def test_mk_img_list(self):
        other_list = img_utils.mk_img_list("sample_data/other")
        pasta_list = img_utils.mk_img_list("sample_data/pasta")
        self.assertEqual(len(other_list), 8)
        self.assertEqual(len(pasta_list), 8)
    
    def test_fetch_json_data(self):
        # TODO: Set Json Data
        pass
    
    def test_fetch_xml_data(self):
        # TODO: Set XML Data
        pass
    
    def test_select_univ_clr(self):
        category_clr_list = img_utils.select_univ_clr(self.category_list)
        self.assertEqual(len(list(category_clr_list.keys())), 
                         len(self.category_list))
        self.assertListEqual(self.category_list,
                             list(category_clr_list.keys()))

if __name__ == "__main__":
    unittest.main()