import numpy as np
import nibabel as nib


def load_nifti(path: str) -> np.ndarray:
    """
    Load a NIfTI MRI file and return the image data as a NumPy array.
    """
    image = nib.load(path)
    data = image.get_fdata()

    return data


def get_middle_slice(volume: np.ndarray, axis: int = 2) -> np.ndarray:
    """
    Extract the middle slice from a 3D MRI volume.
    """
    if volume.ndim != 3:
        raise ValueError(f"Expected a 3D volume, got shape {volume.shape}")

    middle_index = volume.shape[axis] // 2

    if axis == 0:
        return volume[middle_index, :, :]
    elif axis == 1:
        return volume[:, middle_index, :]
    elif axis == 2:
        return volume[:, :, middle_index]
    else:
        raise ValueError("axis must be 0, 1, or 2")


def normalize_image(image: np.ndarray) -> np.ndarray:
    image = image - image.min()
    image = image / image.max()

    return image