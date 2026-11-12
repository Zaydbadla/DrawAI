from pathlib import Path
import numpy as np

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

SAMPLES_PER_CLASS = 1500
RANDOM_SEED = 42


def prepare_data():
    """Select and save random drawings for each class."""

    # Create the output directory if it does not exist
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Initialize a reproducible random number generator
    rng = np.random.default_rng(RANDOM_SEED)

    # Process all .npy files in the raw data directory
    for file_path in sorted(RAW_DIR.glob("*.npy")):
        data = np.load(file_path)

        # Skip classes with insufficient samples
        if len(data) < SAMPLES_PER_CLASS:
            print(f"Not enough samples in {file_path.name}")
            continue

        # Randomly select unique drawings without replacement
        indices = rng.choice(
            len(data),
            size=SAMPLES_PER_CLASS,
            replace=False
        )

        selected_data = data[indices]

        # Save the selected drawings to the processed directory
        output_path = PROCESSED_DIR / file_path.name
        np.save(output_path, selected_data)

        print(f"{file_path.stem}: {len(selected_data)} drawings saved")


if __name__ == "__main__":
    prepare_data()
