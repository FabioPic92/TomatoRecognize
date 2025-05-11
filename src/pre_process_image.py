import json
import os
from collections import defaultdict


import tensorflow as tf

def load_json(json_path):
    with open(json_path) as f:
        data = json.load(f)
    return data

def read_json(json_path):
    data_json = load_json(json_path)

    counts = defaultdict(int)

    id_to_filename = {img["id"]: img["file_name"] for img in data_json["images"]}

    for ann in data_json["annotations"]:
        if ann["category_id"] == 1:  # 1 = l_fully_ripened
            image_id = ann["image_id"]
            filename = id_to_filename[image_id]
            counts[filename] += 1

    # Esempio: stampa i primi 5
    for i, (filename, count) in enumerate(counts.items()):
        print(f"{filename}: {count}")
        if i == 4:
            break