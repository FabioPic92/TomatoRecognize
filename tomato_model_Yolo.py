import torch
import cv2
import matplotlib.pyplot as plt

json_path = "Dataset/annotations/train.json"

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]
    return x * dw, y * dh, w * dw, h * dh

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_path = 'Dataset/train/IMG_1114.jpg'
img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results = model(img_rgb)

predizioni = results.pred[0]  # Per la prima immagine nel batch

# Categorie (classi) di oggetti rilevati
categorie = results.names  # Le classi di oggetti per COCO dataset

# Estrai le bounding boxes, i punteggi e le etichette
boxes = predizioni[:, :-2]  # Le coordinate della bounding box (x1, y1, x2, y2)
confidences = predizioni[:, 4]  # Le probabilità (confidenza)
labels = predizioni[:, 5]  # Le etichette numeriche per le classi (possono essere mappate su categorie)

# Visualizza le informazioni
for box, conf, label in zip(boxes, confidences, labels):
    x1, y1, x2, y2 = box
    label_name = categorie[int(label)]
    print(f"Oggetto: {label_name} | Confidenza: {conf:.2f} | Bounding box: {x1}, {y1}, {x2}, {y2}")