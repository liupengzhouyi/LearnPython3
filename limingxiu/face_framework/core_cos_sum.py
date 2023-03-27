import os
from skimage.metrics import structural_similarity as ssim
from skimage import io
from PIL import Image
import cv2
import numpy

from tools.log import print_log
from tools.resize import image_resize
    

def ssim_core(img_path1: str, img_path2: str, result_path: str):
    
    # 读取两张图片
    img1 = io.imread(img_path1)
    img2 = io.imread(img_path2)
    if img1.shape != img2.shape:
        img1 = image_resize(cv2.imread(img_path1), 361, 361)
        img2 = image_resize(cv2.imread(img_path2), 361, 361)
    r1 = img1[:, :, 0]
    g1 = img1[:, :, 1]
    b1 = img1[:, :, 2]
    r2 = img2[:, :, 0]
    g2 = img2[:, :, 1]
    b2 = img2[:, :, 2]
    if not img_path1.endswith('.jpg') and not img_path1.endswith('.png'): 
        print("image error")
        return
    if not img_path2.endswith('.jpg') and not img_path2.endswith('.png'):
        print("image error")
        return
    # 计算 SSIM 值
    ssim_val_r = ssim(r1, r2, win_size=7, multichannel=True)
    ssim_val_g = ssim(g1, g2, win_size=7, multichannel=True)
    ssim_val_b = ssim(b1, b2, win_size=7, multichannel=True)
    avg = (ssim_val_r + ssim_val_g + ssim_val_b) / 3.0
    return avg
