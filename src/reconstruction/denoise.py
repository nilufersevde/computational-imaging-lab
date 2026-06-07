import numpy as np

from src.degradation.blur import mean_blur_3x3


def simple_denoise(image: np.ndarray) -> np.ndarray:
    """
    Apply simple denoising using a 3x3 mean filter.

    This reduces random noise, but also softens edges.
    """
    if image.ndim != 2:
        raise ValueError(f"Expected a 2D image, got shape {image.shape}")

    return mean_blur_3x3(image)