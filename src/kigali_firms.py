!pip install osmnx pandas --quiet

import os
import osmnx as ox
import pandas as pd
from google.colab import drive

drive.mount('/content/drive')

PROJECT_PATH = "/content/drive/MyDrive/rwanda-nightlights-firm-activity"
RAW_PATH = f"{PROJECT_PATH}/data/raw"

os.makedirs(RAW_PATH, exist_ok=True)

place = "Kigali, Rwanda"
tags = {"amenity": True, "shop": True, "office": True}

gdf = ox.features.features_from_place(place, tags)
df = gdf[["name", "amenity", "shop", "office", "geometry"]].dropna(how="all")

output_file = f"{RAW_PATH}/kigali_firms_raw.csv"
df.to_csv(output_file, index=False)

print(f"Saved to: {output_file}")