import itertools
from pathlib import Path


def mk_img_list(imgs_root):
    '''Return the list of image paths
    # Arguments
    img_root:       input path for fetching image paths
    # Returns
    The list of image paths
    '''
    ir_path = Path(imgs_root)
    return [img_path for img_path in itertools.chain(ir_path.glob('*.jpg'),
                                                     ir_path.glob('*.jpeg'),
                                                     ir_path.glob('*.JPG'),
                                                     ir_path.glob('*.png'),
                                                     ir_path.glob('*.bmp'))]