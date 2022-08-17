


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
    return img


def get_one_style_image_path(image_path: str, image_folder_name: str) -> str:

    print_log("开始获取风格名称为" + image_folder_name + "的文件夹路径")
    style_image_path = os.path.join(image_path, image_folder_name)
    print_log("风格名称为" + image_folder_name + "的文件夹路径为:" + style_image_path)
    return style_image_path

def get_style_images_path(image_path: str, image_folder_name: str, image_type: str) -> list:

    print_log("开始获取风格名称为" + image_folder_name + "的图片路径")
    print_log("该文件夹下的图片文件后缀统一为:" + image_type)
    style_image_path = get_one_style_image_path(image_path=image_path, image_folder_name=image_folder_name)
    images = []
    for index in range(6):
        index = index + 1
        image_name = str(index) + "." + image_type
        temp_path = os.path.join(style_image_path, image_name)
        print_log("第" + str(index) + "张图片的路径为:" + temp_path)
        images.append(temp_path)
    print_log("文件夹:" + style_image_path + "下的图片路径读取完毕，读取到的图片总数为:" + str(len(images)))
    return images

def get_images(image_paths: list, image_folder_name: str) -> list:

    print_log("开始读取" + image_folder_name + "风格的图片...")
    count = len(image_paths)
    print_log("图片数量为:" + str(count))
    images = []
    for item in image_paths:
        print_log("开始读取:" + item)
        temp_image = cv2.imread(item)
        print_log("该图片的大小为:" + str(temp_image.shape))
        temp_image = image_style(temp_image, 250, 250)
        images.append(temp_image)
    print_log("返回" + image_folder_name + "风格的图片{}张".format(str(len(images))))
    return images
    
def add_images(images: list, max_length: int=6):

    print_log("开始纵向拼接图片...")
    print_log("图片数量为{}".format(str(len(images))))
    print_log("支持的图片数量为{}".format(str(max_length)))
    if len(images) != max_length and max_length <= 0 and len(images) < 1:
        print_log("图像数量不对")
        return None
    index = 1
    print_log("取出第{}张图片".format(str(index)))
    target_image = images[0]
    for temp_image in images[1:]:
        index = index + 1
        print_log("取出第{}张图片,拼接在后面".format(str(index)))
        target_image = numpy.concatenate((target_image, temp_image))
    return target_image

def add_row_images(images: list, max_length: int=8):

    print_log("开始横向拼接图片...")
    print_log("图片数量为{}".format(str(len(images))))
    print_log("支持的图片数量为{}".format(str(max_length)))
    if len(images) != max_length and max_length <= 0 and len(images) < 1:
        print_log("图像数量不对")
        return None
    index = 1
    print_log("取出第{}张图片".format(str(index)))
    target_image = images[0]
    for temp_image in images[1:]:
        index = index + 1
        print_log("取出第{}张图片,拼接在后面".format(str(index)))
        target_image = numpy.concatenate((target_image, temp_image), axis=1)
    return target_image

def save_image(image_name: str, image):

    print_log("开始保存图片{}".format(image_name))
    cv2.imwrite(image_name, image)

if __name__ == "__main__":

    image_path = '/Users/liupeng/github/LearnPython3/add_image/add_image_002/images'
    print_log("首先设置文件夹的路径:" + image_path)

    image_type = "png"
    print_log("     设置图片格式为:" + image_type)
    
    old_image_folder_name = 'images'
    print_log("设置原图文件夹名称为:" + old_image_folder_name)
    
    target_image_folder_name = 'target'
    print_log("  目标图文件夹名称为:" + target_image_folder_name)
    
    style_000_folder_name = 'style_000'
    print_log(" 风格0图文件夹名称为:" + style_000_folder_name)
    
    style_001_folder_name = 'style_001'
    print_log(" 风格1图文件夹名称为:" + style_001_folder_name)
    
    style_002_folder_name = 'style_002'
    print_log(" 风格2图文件夹名称为:" + style_002_folder_name)
    
    style_003_folder_name = 'style_003'
    print_log(" 风格3图文件夹名称为:" + style_003_folder_name)
    
    style_004_folder_name = 'style_004'
    print_log(" 风格4图文件夹名称为:" + style_004_folder_name)
    
    style_005_folder_name = 'style_005'
    print_log(" 风格5图文件夹名称为:" + style_005_folder_name)

    all_images = []

    old_image_paths = get_style_images_path(image_path=image_path, image_folder_name=old_image_folder_name, image_type=image_type)
    images = get_images(image_paths=old_image_paths, image_folder_name=old_image_folder_name)
    image_old = add_images(images=images, max_length=6)

    target_image_paths = get_style_images_path(image_path=image_path, image_folder_name=target_image_folder_name, image_type=image_type)
    images = get_images(image_paths=target_image_paths, image_folder_name=target_image_folder_name)
    image_target = add_images(images=images, max_length=6)

    style_000_image_paths = get_style_images_path(image_path=image_path, image_folder_name=style_000_folder_name, image_type=image_type)
    images = get_images(image_paths=style_000_image_paths, image_folder_name=style_000_folder_name)
    style_000_image = add_images(images=images, max_length=6)

    style_001_image_paths = get_style_images_path(image_path=image_path, image_folder_name=style_001_folder_name, image_type=image_type)
    images = get_images(image_paths=style_001_image_paths, image_folder_name=style_001_folder_name)
    style_001_image = add_images(images=images, max_length=6)

    style_002_image_paths = get_style_images_path(image_path=image_path, image_folder_name=style_002_folder_name, image_type=image_type)
    images = get_images(image_paths=style_002_image_paths, image_folder_name=style_002_folder_name)
    style_002_image = add_images(images=images, max_length=6)

    style_003_image_paths = get_style_images_path(image_path=image_path, image_folder_name=style_003_folder_name, image_type=image_type)
    images = get_images(image_paths=style_003_image_paths, image_folder_name=style_003_folder_name)
    style_003_image = add_images(images=images, max_length=6)

    style_004_image_paths = get_style_images_path(image_path=image_path, image_folder_name=style_004_folder_name, image_type=image_type)
    images = get_images(image_paths=style_004_image_paths, image_folder_name=style_004_folder_name)
    style_004_image = add_images(images=images, max_length=6)

    style_005_image_paths = get_style_images_path(image_path=image_path, image_folder_name=style_005_folder_name, image_type=image_type)
    images = get_images(image_paths=style_005_image_paths, image_folder_name=style_005_folder_name)
    style_005_image = add_images(images=images, max_length=6)


    all_images = [image_old, image_target, style_000_image, style_001_image, style_002_image, style_003_image, style_004_image, style_005_image]
    image = add_row_images(images=all_images, max_length=8)
    save_image(image_name="all.png", image=image)
    


    