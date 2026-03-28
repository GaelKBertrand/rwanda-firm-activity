import os
import requests

# Nightlights sample (NOAA VIIRS sample public file)
URL = "https://eogdata.mines.edu/nighttime_light/annual/v21/2022/VNL_v21_npp_2022_global_vcmslcfg_c202303062300.average.dat.tif"
OUTPUT_PATH = "data/raw/nightlights_2022.tif"

os.makedirs("../data/raw", exist_ok=True)

def download_file(url, path):
    print("Downloading data...")
    response = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Download complete.")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_PATH):
        download_file(URL, OUTPUT_PATH)
    else:
        print("File already exists.")