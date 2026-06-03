import numpy as np


def add_gaussian_noise(image: np.ndarray, sigma: float = 0.05) -> np.ndarray:
    """
    Add Gaussian noise to an image.

    Args:
        image: 2D image array with values expected between 0 and 1.
        sigma: Standard deviation of the Gaussian noise.

    Returns:
        Noisy image clipped to the range [0, 1].
    """
    if image.ndim != 2:
        raise ValueError(f"Expected a 2D image, got shape {image.shape}")

    noise = np.random.normal(loc=0.0, scale=sigma, size=image.shape)
    noisy_image = image + noise

    return np.clip(noisy_image, 0.0, 1.0)
