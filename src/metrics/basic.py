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

def peak_signal_to_noise_ratio(
    original: np.ndarray,
    reconstructed: np.ndarray
) -> float:

    mse = mean_squared_error(
        original,
        reconstructed
    )

    if mse == 0:
        return float("inf")

    max_value = np.max(original)

    return 10 * np.log10(
        (max_value ** 2) / mse
    )