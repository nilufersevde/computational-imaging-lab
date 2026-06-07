import numpy as np


def mean_squared_error(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """
    Compute mean squared error between two images.
    Lower is better.
    """
    if original.shape != reconstructed.shape:
        raise ValueError(
            f"Shape mismatch: original {original.shape}, reconstructed {reconstructed.shape}"
        )

    difference = original - reconstructed
    return np.mean(difference ** 2)