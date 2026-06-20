from src.mri.io import load_nifti, get_middle_slice
from src.visualization.plotting import show_image


def main():
    path = "data/sample_mri.nii.gz"

    volume = load_nifti(path)
    print("MRI volume shape:", volume.shape)

    slice_2d = get_middle_slice(volume, axis=2)
    print("Slice shape:", slice_2d.shape)

    show_image(slice_2d, title="Middle MRI Slice")


if __name__ == "__main__":
    main()
