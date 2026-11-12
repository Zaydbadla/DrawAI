import numpy as np
import matplotlib.pyplot as plt

# Load the processed cat drawings
data = np.load("data/processed/cat.npy")

print("Shape:", data.shape)
print("Data type:", data.dtype)

# Create a reproducible random generator
rng = np.random.default_rng(42)

# Select 20 random drawings
indices = rng.choice(len(data), size=20, replace=False)

# Display the 20 random drawings
fig, axes = plt.subplots(4, 5, figsize=(12, 10))

for i, ax in enumerate(axes.flat):
    image = data[indices[i]].reshape(28, 28)

    ax.imshow(
        image,
        cmap="gray",
        vmin=0,
        vmax=255,
        interpolation="bilinear"
    )
    ax.set_title(f"Cat {indices[i]}")
    ax.axis("off")

plt.tight_layout()
plt.show()