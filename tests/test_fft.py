import numpy as np
import pytest
from src.fft.transforms import fft2c, ifft2c

def test_fourier_invertibility_and_energy():
    np.random.seed(42)
    original = np.random.randn(256, 256).astype(np.float32)

    kspace = fft2c(original)
    reconstructed = ifft2c(kspace)

    np.testing.assert_allclose(original, reconstructed.real, rtol=1e-5, atol=1e-5)

    energy_image = np.sum(np.abs(original) ** 2)
    energy_kspace = np.sum(np.abs(kspace) ** 2)

    assert pytest.approx(energy_image, rel=1e-5) == energy_kspace