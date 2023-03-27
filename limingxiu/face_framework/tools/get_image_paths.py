import os


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