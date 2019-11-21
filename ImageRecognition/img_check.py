import itertools
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image
from skimage.io import imread, imsave

class ImgCheck:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        
    def mk_img_list(self, imgs_root=None):
        '''Return the list of image paths
        # Arguments
        img_root:       input path for fetching image paths
        # Returns
        The list of image paths
        '''
        if not imgs_root:
            imgs_root = self.root_path
        ir_path = Path(imgs_root)
        return [img_path for img_path in itertools.chain(ir_path.glob('*.jpg'), 
                                                         ir_path.glob('*.jpeg'),
                                                         ir_path.glob('*.JPG'),  
                                                         ir_path.glob('*.png'), 
                                                         ir_path.glob('*.bmp'))]
        
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
        if self.mk_img_list(dr_path):
            img_tree_list.append(dr_path)
        else:
            for dr in dr_path.glob("*"):
                img_tree_list.extend(self.mk_img_tree(dr))
        return img_tree_list

    def rec_random_pick_imgs(self, data_root=None):
        '''Pick images randomly from data_root
        # Arguments
        data_root:      the root of data which wanted to show image
        # Returns
        imgs_dict:      the dictionary which has 
                            Key:    the image path
                            Value:  image
        '''
        data_tree = self.mk_img_tree(data_root)
        imgs_dict = {}
        for dt in data_tree:
            ip_list = self.mk_img_list(dt)
            ip_len = len(ip_list)
            ip_img = imread(ip_list[np.random.randint(ip_len)])
            imgs_dict[dt] = ip_img
        return imgs_dict
            
    
if __name__ == "__main__":
    data_root_path = Path("sample_data")
    ic = ImgCheck(data_root_path)
    tree_result = ic.mk_img_tree()
    print(tree_result)
    
    for tr in tree_result:
        print(ic.mk_img_list(tr))
        
    print(ic.rec_random_pick_imgs(data_root_path))