import os
from skimage.metrics import structural_similarity as ssim
from skimage import io
from PIL import Image
import os
import cv2
import numpy

def print_log(info: str) -> bool:

    print(info)
    return True


def image_style(image, width, height):

    print_log("对图片进行个性化处理...")
    print_log("重新设置图片大小为[width:{}, height:{}]".format(str(width), str(height)))
    img = cv2.resize(image, (width, height))
    print(type(img))
    return img

# def save_image(image_name: str, image):

#     print_log("开始保存图片{}".format(image_name))
#     cv2.imwrite(image_name, image)
    

def ssim_core(img_path1: str, img_path2: str):
    
    # 读取两张图片
    img1 = io.imread(img_path1)
    img2 = io.imread(img_path2)
    r1 = img1[:, :, 0]
    g1 = img1[:, :, 1]
    b1 = img1[:, :, 2]
    r2 = img2[:, :, 0]
    g2 = img2[:, :, 1]
    b2 = img2[:, :, 2]
    if r1.shape != r2.shape or g1.shape != g2.shape or b1.shape != b2.shape:
        # save_image(img_path1, image_style(cv2.imread(img_path1), 361, 361))
        # save_image(img_path2, image_style(cv2.imread(img_path2), 361, 361))
        # img1 = io.imread(img_path1)
        # img2 = io.imread(img_path2)
        img1 = image_style(cv2.imread(img_path1), 361, 361)
        img2 = image_style(cv2.imread(img_path2), 361, 361)
        r1 = img1[:, :, 0]
        g1 = img1[:, :, 1]
        b1 = img1[:, :, 2]
        r2 = img2[:, :, 0]
        g2 = img2[:, :, 1]
        b2 = img2[:, :, 2]
    if not img_path1.endswith('.jpg') and not img_path1.endswith('.png') and not img_path2.endswith('.jpg') and not img_path2.endswith('.png'): 
        print("image error")
        return
    # 计算 SSIM 值
    ssim_val_r = ssim(r1, r2, win_size=7, multichannel=True)
    ssim_val_g = ssim(g1, g2, win_size=7, multichannel=True)
    ssim_val_b = ssim(b1, b2, win_size=7, multichannel=True)
    avg = (ssim_val_r + ssim_val_g + ssim_val_b) / 3.0
    
    print("------------------------------------------------------------------------")
    print("source image path:", img_path1)
    print("target image path:", img_path2)
    print(img1.shape)
    print(r2.shape)
    print("SSIM value r:", ssim_val_r)
    print("SSIM value g:", ssim_val_g)
    print("SSIM value b:", ssim_val_b)
    print("Average SSIM value:", avg)
    print("------------------------------------------------------------------------")
    
    return avg


def get_folder_images_path(folder_path: str) -> list:

    images_path = []
    for item in os.listdir(folder_path):
        item = os.path.join(folder_path, item)
        images_path.append(item)
        # print(item)
    return images_path

def get_result_images_path(folder_path: str, source_image_path: str) -> list:

    source_images = get_folder_images_path(folder_path=source_image_path)
    images_maps = []
    for item in source_images:
        image_folder_path = os.path.join(folder_path, item.split('.')[0].split('/')[-1])
        # print(image_folder_path)
        if not os.path.exists(image_folder_path):
            # print("No target folder:" + image_folder_path)
            continue
        new_image_path = []
        for image_name in os.listdir(image_folder_path):
            temp_result_image_path = os.path.join(image_folder_path, image_name)
            # temp_map = {item: temp_result_image_path}
            temp_map = [temp_result_image_path, item]
            new_image_path.append(temp_map)
            # print(temp_map)
        images_maps.append(new_image_path)

    return images_maps


source_image_folder = "/Users/pengliu/Code/LearnPython3/limingxiu/ssim4face/non-makeup"
result_image_folder = "/Users/pengliu/Code/LearnPython3/limingxiu/ssim4face/psgan/result"

maps = get_result_images_path(folder_path=result_image_folder, source_image_path=source_image_folder)

for one_source_list in maps:
    for item in one_source_list:
        # print(item)
        img_path1 = item[0]
        img_path2 = item[1]
        if os.path.exists(img_path1) and os.path.exists(img_path2):
            print(img_path1)
            print(img_path2)
            ssim_core(img_path1=img_path1, img_path2=img_path2)