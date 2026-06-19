import numpy as np

from src.fft.transforms import fft2c, ifft2c


def wiener_denoise(image: np.ndarray, noise_power: float = 0.01) -> np.ndarray:
    """
    Apply a simple Wiener-like denoising filter in frequency space.

    This suppresses weak frequency components that are more likely to be noise.
    """
    if image.ndim != 2:
        raise ValueError(f"Expected a 2D image, got shape {image.shape}")

    kspace = fft2c(image)

    power_spectrum = np.abs(kspace) ** 2

    wiener_filter = power_spectrum / (power_spectrum + noise_power)

    filtered_kspace = wiener_filter * kspace

    denoised = ifft2c(filtered_kspace)

    return np.clip(denoised.real, 0.0, 1.0)
