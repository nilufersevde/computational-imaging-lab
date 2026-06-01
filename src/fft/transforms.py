import numpy as np

def fft2c(image: np.ndarray) -> np.ndarray:
    """
    Computes the 2D Centered Fast Fourier Transform (Orthonormal).
    Moves the zero-frequency component to the center of the spectrum.
    
    Args:
        image: A 2D complex or float NumPy array (Image Space).
        
    Returns:
        A 2D complex NumPy array (k-Space / Frequency Space).
    """
    if image.ndim != 2:
        raise ValueError(f"Expected a 2D array, but got shape {image.shape}")
        
    # 1. Shift the center of the image space to the corners before FFT
    # 2. Compute the standard 2D FFT with orthonormal normalization
    # 3. Shift the corners back to the center of the frequency space
    return np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(image), norm="ortho"))


def ifft2c(kspace: np.ndarray) -> np.ndarray:
    """
    Computes the 2D Centered Inverse Fast Fourier Transform (Orthonormal).
    Transforms k-space data back to image space seamlessly.
    
    Args:
        kspace: A 2D complex NumPy array (k-Space).
        
    Returns:
        A 2D complex NumPy array (Image Space).
    """
    if kspace.ndim != 2:
        raise ValueError(f"Expected a 2D array, but got shape {kspace.shape}")
        
    # 1. Shift the center of the frequency space to the corners before IFFT
    # 2. Compute the standard 2D IFFT with orthonormal normalization
    # 3. Shift the corners back to the center of the image space
    return np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(kspace), norm="ortho"))