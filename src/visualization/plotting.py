import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title=None, cmap="gray"):
    plt.figure(figsize=(5, 5))
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    if title:
        plt.title(title)
    plt.show()


def show_images(images, titles=None, cmap="gray"):
    n = len(images)
    plt.figure(figsize=(5 * n, 5))

    for i, image in enumerate(images):
        plt.subplot(1, n, i + 1)
        plt.imshow(image, cmap=cmap)
        plt.axis("off")

        if titles:
            plt.title(titles[i])

    plt.show()


def show_kspace_magnitude(kspace, title="k-space magnitude"):
    magnitude = np.log1p(np.abs(kspace))

    plt.figure(figsize=(5, 5))
    plt.imshow(magnitude, cmap="gray")
    plt.axis("off")
    plt.title(title)
    plt.show()