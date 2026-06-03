import numpy as np

from src.fft.transforms import fft2c
from src.visualization.plotting import show_images, show_kspace_magnitude
from src.degradation.noise import add_gaussian_noise


def create_fake_image(size=256):
    image = np.zeros((size, size), dtype=np.float32)

    # White square in the middle
    image[90:166, 90:166] = 1.0

    return image


def main():
    image = create_fake_image()
    noisy_image = add_gaussian_noise(image, sigma=0.10)

    kspace = fft2c(noisy_image)

    show_images(
        [image, noisy_image],
        ["Original synthetic image", "Noisy image"]
    )

    show_kspace_magnitude(
        kspace,
        title="Centered k-space magnitude of noisy image"
    )


if __name__ == "__main__":
    main()


