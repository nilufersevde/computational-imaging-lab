import streamlit as st
from src.mri.io import load_nifti, get_middle_slice, normalize_image
from src.degradation.blur import mean_blur_3x3
from src.degradation.noise import add_gaussian_noise
import matplotlib.pyplot as plt
import tempfile
from src.reconstruction.wiener import wiener_denoise 

from src.metrics.basic import (
    mean_squared_error,
    peak_signal_to_noise_ratio
)

st.set_page_config(
    page_title="Computational Imaging Lab",
    page_icon="🧠",
    layout="wide"
)

st.title("Computational Imaging Lab")

st.divider()

st.caption(
    "Interactive MRI denoising and quantitative image quality evaluation."
)

st.write(
    """
    Upload a brain MRI in NIfTI format and interactively explore Gaussian noise and denoising algorithms.
    """
)

uploaded_file = st.file_uploader(
    "Upload MRI",
    type=["nii", "gz"]
)

noise_sigma = st.slider(
    "Noise Level",
    0.0,
    0.20,
    0.05,
    0.01
)

denoising_method = st.radio(
    "Denoising Method",
    ["Mean Filter", "Wiener Filter"]
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".nii.gz"
    ) as temp_file:

        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name
    volume = load_nifti(temp_path)
    volume = normalize_image(volume)

    slice_2d = get_middle_slice(volume)
    noisy_slice = add_gaussian_noise(
        slice_2d,
        sigma=noise_sigma
    )
    if denoising_method == "Mean Filter":
        denoised_slice = mean_blur_3x3(noisy_slice)

    elif denoising_method == "Wiener Filter":
        denoised_slice = wiener_denoise(noisy_slice, noise_power=0.1)

    mse = mean_squared_error(
        slice_2d,
        denoised_slice
    )

    psnr = peak_signal_to_noise_ratio(
        slice_2d,
        denoised_slice
    )

    col1, col2, col3 = st.columns(3)
    st.divider()

    with col1:
        st.markdown("<h3 style='text-align:center;'>Original</h3>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.imshow(slice_2d.T, cmap="gray", origin="lower")
        ax.axis("off")
        st.pyplot(fig)

    with col2:
        st.markdown("<h3 style='text-align:center;'>Noisy</h3>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.imshow(noisy_slice.T, cmap="gray", origin="lower")
        ax.axis("off")
        st.pyplot(fig)

    with col3:
        st.markdown(
            f"<h3 style='text-align:center;'>{denoising_method}</h3>",
            unsafe_allow_html=True
        )
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.imshow(denoised_slice.T, cmap="gray", origin="lower")
        ax.axis("off")
        st.pyplot(fig)


    st.subheader("Evaluation")

    st.markdown(
    f"""
    | Metric | Value |
    |---|---:|
    | MSE | `{mse:.6f}` |
    | PSNR | `{psnr:.2f} dB` |
    """
    )
else:
    st.info("Please upload a .nii or .nii.gz file.")

st.divider()

st.subheader("Project Features")

st.markdown("""
This demo demonstrates:

- MRI loading from NIfTI (.nii/.nii.gz)
- Gaussian noise simulation
- Mean filtering
- Wiener filtering
- Quantitative evaluation using MSE and PSNR
""")
st.caption("Developed by Nilüfer Sevde Özdemir")