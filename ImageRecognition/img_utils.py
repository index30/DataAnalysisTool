import itertools
import json
from pathlib import Path

# 赤, 黄, 緑, ピンク, 青, 茶, オレンジ, 空色, 明るい紫, クリーム
# グレー, 明るい緑
UNIV_CLR_LIST = [(255, 40, 0), (250, 245, 0), (53, 161, 107),
                 (255, 153, 160), (0, 65, 255), (102, 51, 0),
                 (255, 153, 0), (102, 204, 255), (199, 178, 222),
                 (255, 255, 153), (127, 135, 143), (135, 231, 176)]

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

def fetch_json_data(json_path):
    '''Fetch the data of json
    # Arguments
    json_path:      input path for fetching json path
    '''
    with open(Path(json_path).as_posix(), 'r') as json_file:
        data = json.load(json_file)
    return data

def select_univ_clr(target_category_list):
    '''Return color list correspond to UNIV_CLR_LIST
    # Argument
    target_category:        the list of category
    # Return
    category_clr_dict       the dict of color and category
    '''
    category_clr_dict = {}
    for tc, ucl in zip(target_category_list, UNIV_CLR_LIST):
        category_clr_dict[tc] = ucl    
    return category_clr_dict