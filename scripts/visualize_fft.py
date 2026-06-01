import numpy as np

from src.fft.transforms import fft2c
from src.visualization.plotting import show_images, show_kspace_magnitude


def create_fake_image(size=256):
    image = np.zeros((size, size), dtype=np.float32)

    # White square in the middle
    image[90:166, 90:166] = 1.0

    return image


def main():
    image = create_fake_image()

    kspace = fft2c(image)

    show_images(
        [image],
        ["Original synthetic image"]
    )

    show_kspace_magnitude(
        kspace,
        title="Centered k-space magnitude"
    )


if __name__ == "__main__":
    main()


