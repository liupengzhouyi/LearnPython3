import os
from skimage.metrics import structural_similarity as ssim
from skimage import io
from PIL import Image
import os
import cv2
import numpy
import os

from tools.log import print_log

def image_resize(image, width, height) -> numpy.ndarray:

    # print_log("对图片进行个性化处理...")
    # print_log("重新设置图片大小为[width:{}, height:{}]".format(str(width), str(height)))
    img = cv2.resize(image, (width, height))
    return img