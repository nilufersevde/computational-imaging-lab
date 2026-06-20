import cv2
import numpy as np

def mean_blur_3x3(image: np.ndarray) -> np.ndarray:
    """
    Apply a simple 3x3 mean blur manually.

    Each pixel is replaced by the average of its 3x3 neighborhood.
    """
    if image.ndim != 2:
        raise ValueError(f"Expected a 2D image, got shape {image.shape}")

    kernel = np.ones((3, 3), dtype=np.float32) / 9.0

    padded = np.pad(image, pad_width=1, mode="edge")
    blurred = np.zeros_like(image, dtype=np.float32)

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            neighborhood = padded[row:row + 3, col:col + 3]
            blurred[row, col] = np.sum(neighborhood * kernel)

    return blurred


"""def apply_gaussian_blur(
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
    )"""
