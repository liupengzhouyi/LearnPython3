from cleanfid import fid


def fid_core(source_image_path: str, target_image_path: str):
    
    fid_value = fid.compute_fid(source_image_path, target_image_path)
    return fid_value
