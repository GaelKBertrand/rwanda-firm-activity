import rasterio
import numpy as np

INPUT_PATH = "data/raw/nightlights_2022.tif"

def load_raster(path):
    with rasterio.open(path) as src:
        data = src.read(1)
        profile = src.profile
    return data, profile

def clean_data(data):
    data = np.where(data < 0, 0, data)
    return data

def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

if __name__ == "__main__":
    data, profile = load_raster(INPUT_PATH)
    data = clean_data(data)
    data = normalize(data)

    np.save("data/processed/nightlights_clean.npy", data)
    print("Preprocessing complete.")