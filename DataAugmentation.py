
# coding: utf-8

# # 图像增强类
# ## 版本：
# 0.1
# ## 功能简介:
# 实现图像的读取、缩放、显示、裁剪、平移、旋转、仿射变换及投影变换

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt
import os

class DataAugmentation():
    def __init__(self):
        self.path = ''
        
    # 读取一个图片文件
    def read_file(self, path):
        self.file = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        self.path = path
            
    # 打印原始图像
    def get_image(self, gray = False):
        if os.path.exists(self.path):
            if gray == True:
                img_ret = cv2.cvtColor(self.file, cv2.COLOR_BGR2GRAY)                
            else:
                img_ret = self.file

            return img_ret
        else:
            print('File does not exit!Make sure read_file() reads the existing file.')   
    
    # 显示图片
    def show_image(self, data, title='image'):
        cv2.imshow(title, data)
        cv2.waitKey (0) 
        cv2.destroyAllWindows() # 释放窗口
            
    # 图片切片
    def crop_image(self, left, up, right, bottom):
        img_crop = self.file[up:bottom, left:right]
        return img_crop
    
    # 获取三个通道数据
    def get_diff_channels(self):
        # color splite
        B, G, R = cv2.split(self.file)
        return B, G, R
    
    # 随意调增颜色
    # upper_bound: 随机调整幅度的上界
    # lower_bound: 随机调整幅度的下界
    def random_light_color(self, lower_bound, upper_bound):
        B, G, R = cv2.split(self.file)

        b_rand = random.randint(lower_bound, upper_bound)

        if b_rand == 0:
            pass
        elif b_rand > 0:
            lim = 255 - b_rand
            B[B > lim] = 255
            B[B <= lim] = (b_rand + B[B <= lim]).astype(self.file.dtype)
        else:
            lim = 0 - b_rand
            B[B < lim] = 0
            B[B >= lim] = (b_rand + B[B >= lim]).astype(self.file.dtype)        

        g_rand = random.randint(lower_bound, upper_bound)
        if g_rand == 0:
            pass
        elif g_rand > 0:
            lim = 255 - g_rand
            G[G > lim] = 255
            G[G <= lim] = (g_rand + G[G <= lim]).astype(self.file.dtype)
        else:
            lim = 0 - g_rand
            G[G < lim] = 0
            G[G >= lim] = (g_rand + G[G >= lim]).astype(self.file.dtype)     

        r_rand = random.randint(lower_bound, upper_bound)
        if r_rand == 0:
            pass
        elif r_rand > 0:
            lim = 255 - r_rand
            R[R > lim] = 255
            R[R <= lim] = (r_rand + R[R <= lim]).astype(self.file.dtype)
        else:
            lim = 0 - r_rand
            R[R < lim] = 0
            R[R >= lim] = (r_rand + R[R >= lim]).astype(self.file.dtype)     

        img_merge = cv2.merge((B, G, R))
        return img_merge
    
    # gamma 校正
    def adjust_gamma(self, gamma=1.0):
        inv_gamma = 1 / gamma
        table = ((np.arange(256) / 255.0) ** inv_gamma) * 255
        table = table.astype('uint8')
        # LUT 是查表的意思，实现了 img中数值的table表的查找
        return cv2.LUT(self.file, table)
    
    # resize的参数是 宽和高    
    def resize(self, width, height):
        img_resize = cv2.resize(self.file, (int(width), int(height)))
        return img_resize
    
    # 图像亮度均衡
    def brightEqualize(self):
        img_yuv = cv2.cvtColor(self.file, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        return img_output
    
    # 旋转, 输入旋转的中心坐标，角度，缩放
    def rotate(self, r_x, r_y, angle, scale):
        # rotation , 以图片中心旋转
        M = cv2.getRotationMatrix2D((r_x, r_y ), angle, scale)
        # 仿射变换
        img_rotate = cv2.warpAffine(self.file, M, (int(self.file.shape[1] * scale), int(self.file.shape[0] * scale)))
        return img_rotate
    
    # 仿射变换
    def affineTransform(self, pts1, pts2):
        M = cv2.getAffineTransform(pts1, pts2)
        img_dst = cv2.warpAffine(self.file, M, (self.file.shape[1], self.file.shape[0]))
        return img_dst
    
    # 投影变换
    def perspectiveTransform(self, pts1, pts2):
        M_wrap = cv2.getPerspectiveTransform(pts1, pts2)
        img_pers = cv2.warpPerspective(self.file, M_wrap, (self.file.shape[1], self.file.shape[0]))
        return img_pers




