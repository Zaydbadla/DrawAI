
import numpy as np

# Load cat drawings from the Quick Draw dataset
daten = np.load("data/raw/cat.npy")

# Display information about the dataset
print(type(daten))
print(daten.shape)
print(daten.dtype)
