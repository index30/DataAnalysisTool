import itertools
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image
from skimage.io import imread, imsave

import img_utils

'''img_check.py
About
画像関連を検証するためのclass

Caution
画像処理や画像等の取得は別関数に分ける
'''
class ImgCheck:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        
    def mk_img_tree(self, data_root=None):
        '''Return the list of image roots
        # Arguments
        data_root:      input path for data
        # Returns
        The list of image roots
        '''
        if not data_root:
            data_root = self.root_path
        dr_path = Path(data_root)
        img_tree_list = []
        if img_utils.mk_img_list(dr_path):
            img_tree_list.append(dr_path)
        else:
            for dr in dr_path.glob("*"):
                img_tree_list.extend(self.mk_img_tree(dr))
        return img_tree_list

    def rec_random_pick_imgs(self, data_root=None, fixed_val=None):
        '''Pick images randomly from data_root
        data_rootに設定したpathから各ディレクトリ内に存在する画像を1つずつランダムにピックアップ
        # Arguments
        data_root:      the root of data which wanted to show image
        # Returns
        imgs_dict:      the dictionary which has 
                            Key:    the image path
                            Value:  image
        '''
        if not data_root:
            data_root = self.root_path
        data_tree = self.mk_img_tree(data_root)
        imgs_dict = {}
        for dt in data_tree:
            ip_list = img_utils.mk_img_list(dt)
            ip_len = len(ip_list)
            if ip_len > 0 and not fixed_val:
                img_path = ip_list[np.random.randint(ip_len)]
            else:
                img_path = ip_list[fixed_val]
            ip_img = imread(img_path)
            imgs_dict[img_path] = ip_img
        return imgs_dict
    
    def rec_random_pick_annotations(self, data_root=None, anno_root=None):
        '''
        # Arguments
        data_root:      the root of data which wanted to show image
        anno_root:      the root of data which wanted to show annotation
        
        # Return
        img_anno_dicts: the dicts which have image and annotation path
        
        # Caution
        This method receive only format 'AAAA_(train/test)_(images/annotations)'
            AAAA:                   Any String(or None)
            (train/test):           The purpose of target data
            (images/annotations):   The type of target data
        '''
        if not data_root:
            data_root = self.root_path
        imgs_dict = self.rec_random_pick_imgs(data_root)
        img_anno_dicts = {}
        for i, (img_key, img_val) in enumerate(imgs_dict.items()):
            # Get string "AAAA_(train/test)_(images/annotations)"
            img_rootname_list  = img_key.parent.stem.split("_")
            # Convert (train/test)_images to (train/test)_annotations
            anno_root_name = img_rootname_list[-2] + "_annotations"
            # If you input anno path, this method refer to it
            if not anno_root:
                anno_root = img_key.parents[1]
            anno_path = list(anno_root.glob("*{0}/{1}*".format(anno_root_name, 
                                                               img_key.stem)))[0]
            img_anno_dicts["img_anno{}".format(i)] = {"img_path": img_key,
                                                      "anno_path": anno_path}
        return img_anno_dicts
        
        
if __name__ == "__main__":
    data_root_path = Path("sample_data")
    ic = ImgCheck(data_root_path)
    tree_result = ic.mk_img_tree()
    print(tree_result)
    
    print(ic.rec_random_pick_imgs(data_root_path))