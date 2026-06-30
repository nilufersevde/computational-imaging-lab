import streamlit as st
from src.mri.io import load_nifti, get_middle_slice, normalize_image
from src.visualization.plotting import show_images
import matplotlib.pyplot as plt
import tempfile
import os

st.set_page_config(
    page_title="Computational Imaging Lab",
    page_icon="🧠",
    layout="wide"
)

st.title("Computational Imaging Lab")

st.header("MRI Denoising")

st.write(
    """
    Welcome to the MRI Denoising Demo.

    This application demonstrates basic image-processing techniques
    on brain MRI images using:
    - Gaussian Noise
    - Mean Filtering
    - Wiener Filtering
    """
)

uploaded_file = st.file_uploader(
    "Upload a NIfTI MRI file",
    type=["nii", "gz"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully.")

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".nii.gz"
    ) as temp_file:

        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name
        volume = load_nifti(temp_path)

        slice_2d = get_middle_slice(volume)
        slice_2d = normalize_image(slice_2d)

        st.write(uploaded_file)
        st.write(type(uploaded_file))

        fig, ax = plt.subplots(figsize=(5, 7))
        ax.imshow(slice_2d.T, cmap="gray", origin="lower")
        ax.set_title("Middle MRI Slice")
        ax.axis("off")

        st.pyplot(fig)
else:
    st.info("Please upload a .nii or .nii.gz file.")

