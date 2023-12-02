#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
import cv2
import json
import matplotlib.pyplot as plt
import argparse


# In[ ]:


def main():
    parser = argparse.ArgumentParser(description='Labelme json to mask jpg')
    parser.add_argument('--json_path', type=str, default='./labelme/', help='Labelme json path')
    parser.add_argument('--mask_image_path', type=str, default='./Mask/', help='Mask image path')

    args = parser.parse_args()
    
    print('Input arguments:')
    for key, value in vars(args).items():
        print('\t{}: {}'.format(key, value))
    print('')
    
    file_path=args.json_path
    mask_path=args.mask_image_path
    
    img_list=[s for s in os.listdir(file_path) if '.jpg' in s]
    json_list=[s for s in os.listdir(file_path) if '.json' in s]
    
    for img in img_list:
        raw_img=cv2.cvtColor(cv2.imread(os.path.join(file_path,img), 1), cv2.COLOR_BGR2RGB)     
        with open(os.path.join(file_path,[s for s in json_list if img.split('.jpg')[0] in s][0])) as f:
            tmp_json = json.load(f)

            # Generate background
            background_img = np.zeros(raw_img.shape)

            ## Mask definition
            mask_color = (1, 1, 1) 

            for area in tmp_json['shapes']:
                tmp_area=area['points']
                tmp_area=np.array(tmp_area,np.int32)
                cv2.fillPoly(background_img, [tmp_area], mask_color)
            cv2.imwrite(os.path.join(mask_path,'Mask_'+img) , background_img)


# In[ ]:


if __name__ == '__main__':
    main()


# In[ ]:




