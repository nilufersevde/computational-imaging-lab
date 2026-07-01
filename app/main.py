import streamlit as st
from src.mri.io import load_nifti, get_middle_slice, normalize_image
from src.degradation.blur import mean_blur_3x3
from src.degradation.noise import add_gaussian_noise
from src.visualization.plotting import show_images
import matplotlib.pyplot as plt
import tempfile
from src.reconstruction.wiener import wiener_denoise 
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

noise_sigma = st.slider(
    "Gaussian Noise Level",
    min_value=0.0,
    max_value=0.20,
    value=0.05,
    step=0.01
)

denoising_method = st.radio(
    "Choose Denoising Method",
    ["Mean Filter", "Wiener Filter"]
)

st.write("Selected method:", denoising_method)



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
        noisy_slice = add_gaussian_noise(
            slice_2d,
            sigma=noise_sigma
        )
        if denoising_method == "Mean Filter":
            denoised_slice = mean_blur_3x3(noisy_slice)

        elif denoising_method == "Wiener Filter":
            denoised_slice = wiener_denoise(noisy_slice, noise_power=0.1)

        st.write(uploaded_file)
        st.write(type(uploaded_file))

        fig, ax = plt.subplots(figsize=(5, 7))
        ax.imshow(slice_2d.T, cmap="gray", origin="lower")
        ax.set_title("Middle MRI Slice")
        ax.axis("off")

        st.pyplot(fig)

        fig_noisy, ax = plt.subplots(figsize=(5, 7))
        ax.imshow(noisy_slice.T, cmap="gray", origin="lower")
        ax.set_title("Noisy")
        ax.axis("off")

        st.pyplot(fig_noisy)

        fig_denoised, ax = plt.subplots(figsize=(5, 7))
        ax.imshow(denoised_slice.T, cmap="gray", origin="lower")
        ax.set_title(f"Denoised: {denoising_method}")
        ax.axis("off")

        st.pyplot(fig_denoised)
else:
    st.info("Please upload a .nii or .nii.gz file.")