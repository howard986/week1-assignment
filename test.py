from DataAugmentation import DataAugmentation
import numpy as np
import random

data_aug = DataAugmentation()
data_aug.read_file('timg.jpg')
# 返回灰度图像，并显示
data_aug.show_image(data_aug.get_image(gray=True), 'gray image')
# 返回图像，并显示
data_aug.show_image(data_aug.get_image(gray=False), 'original image')
# 图片切片
img_crop = data_aug.crop_image(30, 40, 600, 300)
data_aug.show_image(img_crop, 'crop image')
# 获取B, G, R 三个通道数据
b, g, r = data_aug.get_diff_channels()
data_aug.show_image(g, 'split channl, g channel')
# 随意调整颜色
# upper_bound: 随机调整幅度的上界
# lower_bound: 随机调整幅度的下界
image_merge = data_aug.random_light_color(-50, 100)
data_aug.show_image(image_merge, 'random adjust color')
# gamma校正
img_brighter = data_aug.adjust_gamma(gamma = 2.0)
data_aug.show_image(img_brighter, 'adjust gamma ')
# 调整大小
image_resize = data_aug.resize(1000, 500)
data_aug.show_image(image_resize, 'resize 1000, 500')
# 图像亮度均衡
image_bright_equa = data_aug.brightEqualize()
data_aug.show_image(image_bright_equa, 'bright equalize')
# 图像旋转，缩放
image_rotate= data_aug.rotate(20, 50, 30, 1)
data_aug.show_image(image_rotate, 'rotate and resize')

# 仿射变换
data = data_aug.get_image(gray=False)
rows, cols, chs = data.shape
pts1 = np.float32([[0,0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.6], [cols * 0.1, rows * 0.8]])
img_dst = data_aug.affineTransform(pts1, pts2)
data_aug.show_image(img_dst, 'affine transform')

# 投影变换
data = data_aug.get_image(gray=False)
height, width, channels = data.shape
random_margin = 60
x1 = random.randint(-random_margin, random_margin)
y1 = random.randint(-random_margin, random_margin)
x2 = random.randint(width - random_margin - 1, width - 1)
y2 = random.randint(-random_margin, random_margin)
x3 = random.randint(width - random_margin - 1, width - 1)
y3 = random.randint(height - random_margin - 1, height - 1)
x4 = random.randint(-random_margin, random_margin)
y4 = random.randint(height - random_margin - 1, height - 1)

dx1 = random.randint(-random_margin, random_margin)
dy1 = random.randint(-random_margin, random_margin)
dx2 = random.randint(width - random_margin - 1, width - 1)
dy2 = random.randint(-random_margin, random_margin)
dx3 = random.randint(width - random_margin - 1, width - 1)
dy3 = random.randint(height - random_margin - 1, height - 1)
dx4 = random.randint(-random_margin, random_margin)
dy4 = random.randint(height - random_margin - 1, height - 1)

pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
img_dst = data_aug.perspectiveTransform(pts1, pts2)
data_aug.show_image(img_dst, 'perspective transform')