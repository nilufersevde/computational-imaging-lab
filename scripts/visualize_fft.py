import numpy as np

from src.fft.transforms import fft2c
from src.visualization.plotting import show_images, show_kspace_magnitude
from src.degradation.noise import add_gaussian_noise
"from src.degradation.blur import apply_gaussian_blur"
from src.degradation.blur import mean_blur_3x3


def create_fake_image(size=256):
    image = np.zeros((size, size), dtype=np.float32)

    # White square in the middle
    image[90:166, 90:166] = 1.0
    
    return image


def main():
    image = create_fake_image()
    blurred_image = mean_blur_3x3(image)

    kspace_original = fft2c(image)
    kspace_blurred = fft2c(blurred_image)

    show_images(
    [image, blurred_image],
    ["Original", "Blurred"]
)

    print("Original center:", image[128, 128])
    print("Blurred center:", blurred_image[128, 128])   

    show_kspace_magnitude(
        kspace_blurred,
        title="Centered k-space magnitude of blurry image"
    )

    show_kspace_magnitude(
        kspace_original,
        title="Centered k-space magnitude of original image"
    
    )

if __name__ == "__main__":
    main()


