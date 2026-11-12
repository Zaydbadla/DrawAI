
from pathlib import Path

import numpy as np


PROCESSED_DIR = Path("data/processed")
SPLIT_DIR = Path("data/splits")

TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
RANDOM_SEED = 42


def split_data():
    """Split each class into training, validation, and test sets."""

    rng = np.random.default_rng(RANDOM_SEED)

    # Create directories for the three datasets
    for split in ("train", "val", "test"):
        (SPLIT_DIR / split).mkdir(parents=True, exist_ok=True)

    # Process each class separately
    for file_path in sorted(PROCESSED_DIR.glob("*.npy")):
        data = np.load(file_path)

        # Shuffle the drawings randomly
        indices = rng.permutation(len(data))
        data = data[indices]

        # Calculate the split boundaries
        train_end = int(len(data) * TRAIN_RATIO)
        val_end = train_end + int(len(data) * VAL_RATIO)

        # Split the data without overlap
        train_data = data[:train_end]
        val_data = data[train_end:val_end]
        test_data = data[val_end:]

        # Save each split separately
        np.save(SPLIT_DIR / "train" / file_path.name, train_data)
        np.save(SPLIT_DIR / "val" / file_path.name, val_data)
        np.save(SPLIT_DIR / "test" / file_path.name, test_data)

        print(
            f"{file_path.stem}: "
            f"Train={len(train_data)}, "
            f"Val={len(val_data)}, "
            f"Test={len(test_data)}"
        )


if __name__ == "__main__":
    split_data()
