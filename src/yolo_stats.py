import os
import glob
import matplotlib
matplotlib.use('Agg') 
from collections import Counter
import matplotlib.pyplot as plt

# Dictionnaire des 80 classes YOLO (COCO)
yolo_classes = {
    0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat',
    9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat',
    16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack',
    25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball',
    33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket',
    39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple',
    48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake',
    56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop',
    64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink',
    72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'
}

def analyze_split(split_name, folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Dossier introuvable : {folder_path}")
        return
    
    files = glob.glob(f"{folder_path}/*.txt")
    print(f"\n--- Analyse {split_name.upper()} ({len(files)} fichiers) ---")
    
    all_objects = []
    objects_per_image = []
    
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            objects_per_image.append(len(lines))
            for line in lines:
                class_id = int(line.split()[0])
                all_objects.append(yolo_classes.get(class_id, 'unknown'))
                
    counts = Counter(all_objects)
    top_50 = counts.most_common(50)
    
    print("Top 5 des objets :")
    for obj, count in top_50[:5]:
        print(f"  - {obj} : {count}")
        
    if objects_per_image:
        moyenne = sum(objects_per_image) / len(objects_per_image)
        print(f"Nombre moyen d'objets par image : {moyenne:.2f}")
    
    # Graphique
    if top_50:
        labels, values = zip(*top_50)
        plt.figure(figsize=(15, 6))
        plt.bar(labels, values, color='skyblue')
        plt.xticks(rotation=90)
        plt.title(f'Top 50 Most Frequent Objects - {split_name.upper()} (YOLO)')
        plt.tight_layout()
        plt.savefig(f'graph1_top50_yolo_{split_name}.png')
        print(f"✅ Graphique sauvegardé : graph1_top50_yolo_{split_name}.png")

# --- LANCEMENT DE L'ANALYSE ---
base_path = 'data/processed/yolo/labels'
analyze_split('train', f'{base_path}/train')
analyze_split('val', f'{base_path}/val')
analyze_split('test', f'{base_path}/test')