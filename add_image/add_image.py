
# 图片拼接
from PIL import Image
import cv2
import numpy

import torch

# 控制打印分割线的开关
add_line = False

def print_log(info: str) -> bool:

    print(info)
    return True

def add_side(image: numpy.ndarray) -> numpy.ndarray:
    pass


def create_images() -> list:

    images = []
    print_log("创建11张图片的数据，以list返回。")
    temp_image = cv2.imread("./image001.png")
    print(temp_image)
    s = temp_image.shape
    print(s)
    w = s[1]
    if add_line:
        h = 30
    else:
        h = 0
    newImg = numpy.full((h, w, 3), 255, numpy.uint8)
    temp_image = numpy.concatenate((newImg, temp_image))
    temp_image = numpy.concatenate((temp_image, newImg))
    for index in range(11):
        images.append(temp_image)
    return images


def add_images(images: list) -> numpy.ndarray:

    if len(images) <= 0:
        return None
    img_out = images[0]
    s = img_out.shape
    h = s[0]
    if add_line:
        w = 30
    else:
        w = 0
    newImg = numpy.full((h, w, 3), 255, numpy.uint8)
    img_out = numpy.concatenate((img_out, newImg), axis=1)
    for item in images[1:10]:
        img_out = numpy.concatenate((img_out, item), axis=1)
        img_out = numpy.concatenate((img_out, newImg), axis=1)
    img_out = numpy.concatenate((img_out, item), axis=1)
    return img_out


img_out = add_images(create_images())
# cv2.imshow("IMG", img_out)
cv2.imwrite("mergeall.jpg", img_out)
# cv2.waitKey(0)

 #横向
# img_out = np.concatenate((image_001, image_002), axis=1)

 # 纵向
# img_out = np.concatenate((image_001, image_002))