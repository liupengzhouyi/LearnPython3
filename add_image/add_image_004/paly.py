#!/usr/bin/env python
#! -*- coding: utf-8 -*-

from distutils.sysconfig import customize_compiler
from PIL import Image
import cv2
import numpy

def print_log(info: str) -> bool:

    print(info)
    return True

def show_image_help():

    print_log("----------x1--------x2---------------------------------")
    print_log("|         |          |                                 |")
    print_log("|         |          |                                 |")
    print_log("y1 ---->  ___________                                  |")
    print_log("|         |          |                                 |")
    print_log("|         |          |                                 |")
    print_log("|         |          |                                 |")
    print_log("|         |          |                                 |")
    print_log("y2 ---->  |__________|                                 |")
    print_log("|                                                      |")
    print_log("|                                                      |")
    print_log("|                                                      |")
    print_log("|                                                      |")
    print_log("--------------------------------------------------------")

def save_image(image_name: str, image):

    print_log("开始保存图片{}".format(image_name))
    cv2.imwrite(image_name, image)

temp_image = cv2.imread("./image.png")
s = temp_image.shape
print("原图的维度为：{}".format(str(temp_image.shape)))

show_image_help()

# 默认数据是标准的点
x1 = 300
x2 = 600

y1 = 100
y2 = 500

print_log("开始设定x1:{}".format(x1))
print_log("开始设定x2:{}".format(x2))
print_log("开始设定y1:{}".format(y1))
print_log("开始设定y2:{}".format(y2))

# 图像颜色
color = (0, 0, 0)
print("设定边框的颜色{}".format(color))
b = 10
print("设定边框的像素厚度{}".format(b))

sub_image_data = temp_image[y1:y2, x1:x2, :]
print("子图的维度为：{}".format(str(sub_image_data.shape)))


width = 400
height = 400
print_log(f"对裁截出来的字图做resize({str(width)}, {str(height)})操作...")
img = cv2.resize(sub_image_data, (width, height))
print_log(f"新图片的size:({str(img.shape)})")
print_log("缓存新的图片数据...")
save_image(image_name="sub_image.png", image=img)

# print_log("保存截取出来的子图")
# save_image(image_name="sub_image.png", image=sub_image_data)
print_log("边框厚度设置为:{}.".format(str(b)))
for i in range(b):
    for dimension in range(3):
        temp_image[y1:y2, x1 + i, dimension] = color[dimension]
        temp_image[y1:y2, x2 - i - 1, dimension] = color[dimension]
        temp_image[y1 + i, x1:x2, dimension] = color[dimension]
        temp_image[y2 - i - 1, x1:x2, dimension] = color[dimension]
print_log("保存画边框的图")
save_image(image_name="new.png", image=temp_image)

print_log("空白区域的大小为{}")

w = sub_image_data.shape[0]
h = sub_image_data.shape[1]
print_log(f"将新图重新resize:({str(w)},{str(h)}).")
sub_img = cv2.resize(img, (h, w))
print_log(f"新图片的size:{str(sub_img.shape)}")

print_log("开始将子图填充在母图的指定位置:")
show_image_help()
print(y2 - y1)
for index in range(x2 - x1):
    # index = index + 1
    # print(index)
    temp_image[y1:y2, x1 + index, :] = sub_img[0:y2 - y1, index, :]

print_log("保存覆盖子图的的图")
save_image(image_name="add_sub_images.png", image=temp_image)

# print_log(f"{str(temp_image[y1:y2, x1, :])}")
# print_log(str(type(temp_image[y1:y2, x1, :])))
# print_log(str(temp_image[y1:y2, x1, :].shape))

# # temp_image[y1:y2, x1, :]
# print_log(str(sub_img[0:y2 - y1, 0, :]))

# temp_image[y1:y2, x1, :] = sub_img[0:y2 - y1, 0, :]
# print_log(f"{str(temp_image[y1:y2, x1, :])}")






