import cv2
import numpy as np


def apply_gaussian_blur(
    image: np.ndarray,
    kernel_size: int = 9,
    sigma: float = 2.0
) -> np.ndarray:
    if image.ndim != 2:
        raise ValueError(
            f"Expected a 2D image, got shape {image.shape}"
        )

    return cv2.GaussianBlur(
        image,
        (kernel_size, kernel_size),
        sigma
    )