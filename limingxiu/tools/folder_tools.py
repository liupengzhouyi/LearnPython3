import os


# 原图片文件夹地址
source_folder_path = r'C:\Users\liupe\code\LearnPython3\limingxiu\demo\source_images'
# 生成图片文件夹地址
target_folder_path = r"C:\Users\liupe\code\LearnPython3\limingxiu\demo\target_images"
# 图片后缀
image_ends = ['.png', '.jpg']


def print_log(info: str, level:str="DEBUG", show: bool=True):

    show = False
    if show:
        print(info)


def get_target_folder_paths(target_folder_path: str) -> list:

    print_log(info="获取生成图片文件夹")
    folder_paths = []
    if not os.path.exists(target_folder_path):
        print_log(info="生成图片文件夹路径不存在")
    else:
        for item in os.listdir(target_folder_path):
            temp_path = os.path.join(target_folder_path, item)
            if not os.path.isdir(temp_path):
                print_log(info=f"{str(item)}非文件夹，跳过。")
            else:
                print_log(info=f"获取文件夹: {str(temp_path)}")
                folder_paths.append(temp_path)
    return folder_paths


def check_tatget_file(file_name: str, file_ends: list=None) -> bool:

    result = False
    if not file_ends:
        result = True
    else:
        for item in file_ends:
            if str(file_name).endswith(item):
                result = True
                break
    print_log(info=f"Check file {file_name} in {str(file_ends)}:{str(result)}")
    return result


def get_source_image_name(source_folder_path: str, file_ends: list=None) -> list:

    print_log(info="获取源文件图片")
    image_names = []
    if not os.path.exists(source_folder_path):
        print_log(info="源图片文件夹路径不存在")
    else:
        for item in os.listdir(source_folder_path):
            print_log(info=f"获取文件: {str(item)}")
            if not os.path.isfile(os.path.join(source_folder_path, item)):
                print_log(info=f"{str(item)}非文件，跳过。")
                continue
            if check_tatget_file(file_name=item, file_ends=file_ends):
                image_names.append(item)
    return image_names


def image_name2path(image_folder_path: str, image_name: str) -> str:

    print_log(info=f"图片名称{image_name}添加到路径{image_folder_path}后")
    image_path = ''
    if not os.path.isdir(image_folder_path):
        print_log(info="图片文件夹路径不存在")
    else:
        image_path = os.path.join(image_folder_path, image_name)
        print_log(info=f"生成：{image_path}")
    return image_path


def batch_image_name2path(image_folder_path: str, image_names: list) -> list:

    image_paths = []
    for item in image_names:
        temp_path = image_name2path(image_folder_path=image_folder_path, image_name=item)
        if temp_path:
            image_paths.append(temp_path)
    return image_paths


def get_image_paths(source_folder_path: str, file_ends: list=None) -> list:

    image_names = get_source_image_name(source_folder_path=source_folder_path, file_ends=image_ends)
    image_paths = batch_image_name2path(image_folder_path=source_folder_path, image_names=image_names)
    return image_paths


def get_folder_path_by_image(image_path: str, folder_paths: list) -> str:

    folder_path = ''
    image_folder_path = os.path.dirname(image_path)
    image_name = image_path.replace(image_folder_path, "")
    image_name = image_name.split('.')[0]
    print_log(info=f"获取图片名称：{image_name}")

    for folder_item in folder_paths:
        temp_folder_path = os.path.dirname(folder_item)
        temp_folder_name = folder_item.replace(temp_folder_path, "")
        print_log(info=f"获取文件夹名称：{temp_folder_name}")
        if temp_folder_name == image_name:
            folder_path = folder_item
    return folder_path


def get_batch_image_folders(image_paths: list, folder_paths: list) -> list:

    image_folder_maps = []

    for image_path in image_paths:
        folder_path = get_folder_path_by_image(image_path=image_path, folder_paths=folder_paths)
        if not folder_path:
            continue
        print_log(info='--------------------------------------------------------------')
        print_log(info=f"|   image path | {image_path}")
        print_log(info=f"|  folder path | {folder_path}")
        print_log(info='--------------------------------------------------------------')
        image_folder_map = {"image_path": image_path, "folder_path": folder_path}
        image_folder_maps.append(image_folder_map)
    return image_folder_maps


def get_image_maps(source_folder_path: str, target_folder_path: str) -> list:

    image_maps = []
    image_paths = get_image_paths(source_folder_path=source_folder_path)
    folders = get_target_folder_paths(target_folder_path=target_folder_path)
    maps = get_batch_image_folders(image_paths=image_paths, folder_paths=folders)
    for item in maps:
        print('------------------------------------------------------------------------')
        print(item)
        for create_image_path in get_image_paths(source_folder_path=item.get('folder_path')):
            print(item.get('image_path'), create_image_path)
            temp_map = {"source_image": item.get('image_path'), "create_image": create_image_path}
            image_maps.append(temp_map)
        print('------------------------------------------------------------------------')
    
    return image_maps
    
    
for item in get_image_maps(source_folder_path, target_folder_path):
    print(item)
