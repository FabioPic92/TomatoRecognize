import json
import random
import os
import shutil

input_json = "../Dataset/annotations/train.json"
src_img_dir = "../Dataset/train/"

train_json = "train.json"
val_json = "val.json"

train_img_dir = "train"
val_img_dir = "val"

val_ratio = 0.2

os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)

with open(input_json, "r") as f:
    data = json.load(f)

images = data["images"]
annotations = data["annotations"]
categories = data["categories"]
info = data.get("info", {})
licenses = data.get("licenses", [])

random.shuffle(images)
val_size = int(len(images) * val_ratio)

val_images = images[:val_size]
train_images = images[val_size:]

# Ottieni set di ID immagine
val_ids = set(img["id"] for img in val_images)
train_ids = set(img["id"] for img in train_images)

# Filtra le annotazioni
train_annotations = [ann for ann in annotations if ann["image_id"] in train_ids]
val_annotations = [ann for ann in annotations if ann["image_id"] in val_ids]

# Scrivi i file COCO
def write_coco_file(filename, images, annotations):
    coco_format = {
        "info": info,
        "licenses": licenses,
        "images": images,
        "annotations": annotations,
        "categories": categories,
    }
    with open(filename, "w") as f:
        json.dump(coco_format, f, indent=4)

write_coco_file(train_json, train_images, train_annotations)
write_coco_file(val_json, val_images, val_annotations)

print(f"Train: {len(train_images)} immagini, {len(train_annotations)} annotazioni")
print(f"Val: {len(val_images)} immagini, {len(val_annotations)} annotazioni")


def copy_images(json_path, target_dir):
    with open(json_path, 'r') as f:
        data = json.load(f)
    for img in data['images']:
        filename = img['file_name']
        src = os.path.join(src_img_dir, filename)
        dst = os.path.join(target_dir, filename)
        if os.path.exists(src):
            shutil.copy2(src, dst)
        else:
            print(f"⚠️ Immagine non trovata: {filename}")

copy_images(train_json, train_img_dir)
copy_images(val_json, val_img_dir)