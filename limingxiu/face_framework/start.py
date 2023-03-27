import os
from skimage.metrics import structural_similarity as ssim

from tools.log import print_log
from tools.get_image_paths import get_result_images_path

from core_ssim import ssim_core
from core_fid import fid_core
from core_rac_face import arc_face_core

def calculate_ssim(image_paths : list) -> float:
    
    count = 0
    sum = 0.0
    for one_source_list in image_paths:
        for item in one_source_list:
            img_path1 = item[0]
            img_path2 = item[1]
            if os.path.exists(img_path1) and os.path.exists(img_path2):
                temp_avg_ssim = ssim_core(img_path1=img_path1, img_path2=img_path2)
                print_log("No." + str(count) + ", SSIM:" + str(temp_avg_ssim))
                sum = sum + temp_avg_ssim
                count = count + 1
    avg_ssim = sum / count
    print_log("---------")
    print_log("Average SSIM:" + str(avg_ssim))
    return avg_ssim


def calculate_fid(image_paths : list) -> float:
    
    count = 0
    sum = 0.0
    for one_source_list in image_paths:
        for item in one_source_list:
            img_path1 = item[0]
            img_path2 = item[1]
            if os.path.exists(img_path1) and os.path.exists(img_path2):
                temp_value = fid_core(source_image_path=img_path1, target_image_path=img_path2)
                print_log("No." + str(count) + ", FID:" + str(temp_value))
                sum = sum + temp_value
                count = count + 1
    avg_ssim = sum / count
    print_log("---------")
    print_log("Average FID:" + str(avg_ssim))
    return avg_ssim


def calculate_arc_face(image_paths : list) -> float:
    
    count = 0
    sum = 0.0
    for one_source_list in image_paths:
        for item in one_source_list:
            img_path1 = item[0]
            img_path2 = item[1]
            if os.path.exists(img_path1) and os.path.exists(img_path2):
                temp_arc_face = arc_face_core(img_path1=img_path1, img_path2=img_path2)
                print_log("No." + str(count) + ", Arc face:" + str(temp_arc_face))
                sum = sum + temp_arc_face
                count = count + 1
    avg_ssim = sum / count
    print_log("---------")
    print_log("Average Arc face:" + str(avg_ssim))
    return avg_ssim


if __name__ == '__main__':
    
    source_image_folder = "/Users/pengliu/Code/LearnPython3/limingxiu/ssim4face/non-makeup"
    result_image_folder = "/Users/pengliu/Code/LearnPython3/limingxiu/ssim4face/psgan/result"
    image_paths = get_result_images_path(folder_path=result_image_folder, source_image_path=source_image_folder)
    
    average_ssim_value = calculate_ssim(image_paths=image_paths)
    average_fid = calculate_fid(image_paths=image_paths)
    average_arc_face = calculate_arc_face(image_paths=image_paths)
    

    