from arcface import ArcFace

def arc_face_core(source_image_path: str, target_image_path: str):

    face_rec = ArcFace.ArcFace()
    emb1 = face_rec.calc_emb(source_image_path)
    emb2 = face_rec.calc_emb(target_image_path)
    value = face_rec.get_distance_embeddings(emb1, emb2)
    return value