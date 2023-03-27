import os
from skimage.metrics import structural_similarity as ssim
from skimage import io
from PIL import Image
import os
import cv2
import numpy
import sys
import os


def print_log(info: str) -> bool:

    print(info)
    return True


def image_style(image, width, height):

    # print_log("对图片进行个性化处理...")
    # print_log("重新设置图片大小为[width:{}, height:{}]".format(str(width), str(height)))
    img = cv2.resize(image, (width, height))
    # print(type(img))
    return img

def save_core(info: str, file_path: str):
    
    open_file = open(file_path, "a")
    open_file.write(info)
    open_file.close()


def save_txt_md(info: str, file_path: str):
    
    txt = file_path
    save_core(info, txt)
    md = file_path.replace(".txt", ".md").replace("result_txt", "result_md")
    save_core(info, md)
    

def ssim_core(img_path1: str, img_path2: str, result_path: str):
    
    # 读取两张图片
    img1 = io.imread(img_path1)
    img2 = io.imread(img_path2)
    if img1.shape != img2.shape:
        img1 = image_style(cv2.imread(img_path1), 361, 361)
        img2 = image_style(cv2.imread(img_path2), 361, 361)
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
    info = "| " + str(avg) + " | " + str(ssim_val_r) + " | " + str(ssim_val_g) + " | " + str(ssim_val_b) + " | " + os.path.basename(img_path2) + " | " + os.path.basename(img_path1) + " |\n"
    save_txt_md(info, result_path)
    return avg


def get_folder_images_path(folder_path: str) -> list:

    images_path = []
    for item in os.listdir(folder_path):
        item = os.path.join(folder_path, item)
        images_path.append(item)
    return images_path


def get_result_images_path(folder_path: str, source_image_path: str) -> list:

    source_images = get_folder_images_path(folder_path=source_image_path)
    images_maps = []
    for item in source_images:
        image_folder_path = os.path.join(folder_path, item.split('.')[0].split('/')[-1])
        if not os.path.exists(image_folder_path):
            continue
        new_image_path = []
        for image_name in os.listdir(image_folder_path):
            temp_result_image_path = os.path.join(image_folder_path, image_name)
            temp_map = [temp_result_image_path, item]
            new_image_path.append(temp_map)
        images_maps.append(new_image_path)

    return images_maps


file_name = os.path.basename(__file__)
target = file_name.replace("ssim_", "").replace(".py", "")
result_folder_name = os.path.dirname(os.path.dirname(__file__))
result_path = os.path.join(result_folder_name, "result_txt", target + ".txt").replace("/.", "")
print("结果保存到" + result_path)

title = "| Average SSIM value | SSIM value r | SSIM value g | SSIM value b | source | psgan |\n"
lane = "| ----- | ----- | --------- | --------- | --------- | ------------------ |\n"
save_txt_md(title, result_path)
save_txt_md(lane, result_path)

source_image_folder = "/Users/pengliu/Code/LearnPython3/limingxiu/ssim4face/non-makeup"
result_image_folder = "/Users/pengliu/Code/LearnPython3/limingxiu/ssim4face/psgan/result"

maps = get_result_images_path(folder_path=result_image_folder, source_image_path=source_image_folder)

for one_source_list in maps:
    for item in one_source_list:
        # print(item)
        img_path1 = item[0]
        img_path2 = item[1]
        # 获取图片名称
        folder_name = img_path2.split('.')[0].split('/')[-1]
        # print(folder_name)
        if folder_name == target:
            folder_name = os.path.basename(img_path1).split('.')[0]
            if os.path.exists(img_path1) and os.path.exists(img_path2):
                # print(img_path1)
                # print(img_path2)
                ssim_core(img_path1=img_path1, img_path2=img_path2, result_path=result_path)