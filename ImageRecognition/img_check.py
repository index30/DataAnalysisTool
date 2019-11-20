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
        
    def mk_img_tree(self, imgs_root=None):
        if not imgs_root:
            imgs_root = self.root_path
        ir_path = Path(imgs_root)
        img_tree_list = []
        if self.mk_img_list(ir_path):
            img_tree_list.append(ir_path)
        else:
            for ir in ir_path.glob("*"):
                img_tree_list.extend(self.mk_img_tree(ir))
        return img_tree_list

        
    def rec_pick_imgs(self, imgs_root=None):
        img_tree = self.mk_img_tree(imgs_root)
        result = {}
        for it in img_tree:
            ip_list = self.mk_img_list(it)
            ip_len = len(ip_list)
            ip_img = imread(ip_list[np.random.randint(ip_len)])
            result[it] = ip_img
        return result
            
    
if __name__ == "__main__":
    data_root_path = Path("sample_data")
    ic = ImgCheck(data_root_path)
    tree_result = ic.mk_img_tree()
    print(tree_result)
    
    for tr in tree_result:
        print(ic.mk_img_list(tr))