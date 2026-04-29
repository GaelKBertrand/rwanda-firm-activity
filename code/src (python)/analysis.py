import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = "data/processed/nightlights_clean.npy"

def load_data(path):
    return np.load(path)

def summarize(data):
    print("Mean light intensity:", np.mean(data))
    print("Max intensity:", np.max(data))
    print("Non-zero pixels:", np.sum(data > 0))

def plot_map(data):
    plt.imshow(data, cmap='hot')
    plt.title("Nightlight Intensity Map")
    plt.colorbar()
    plt.savefig("outputs/maps/nightlights_map.png")
    plt.show()

if __name__ == "__main__":
    data = load_data(DATA_PATH)
    summarize(data)
    plot_map(data)