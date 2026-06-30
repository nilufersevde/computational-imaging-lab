from src.degradation.blur import mean_blur_3x3
from src.mri.io import (
    load_nifti,
    get_middle_slice,
    normalize_image
)
from src.visualization.plotting import show_images
from src.degradation.noise import add_gaussian_noise
from src.metrics.basic import mean_squared_error
from src.metrics.basic import peak_signal_to_noise_ratio
from src.reconstruction.wiener import wiener_denoise



def main():
    path = "data/sample_mri.nii.gz"

    volume = load_nifti(path)
    print("MRI volume shape:", volume.shape)

    slice_2d = get_middle_slice(volume)
    slice_2d = normalize_image(slice_2d)
    noisy_slice = add_gaussian_noise(slice_2d, sigma=0.10)
    mean_denoised = mean_blur_3x3(noisy_slice)
    wiener_denoised = wiener_denoise(noisy_slice, noise_power=0.03)
    print("MSE noisy:", mean_squared_error(slice_2d, noisy_slice))
    print("MSE mean:", mean_squared_error(slice_2d, mean_denoised))
    print("PSNR noisy:", peak_signal_to_noise_ratio(slice_2d, noisy_slice))
    print("PSNR mean:", peak_signal_to_noise_ratio (slice_2d, mean_denoised))
    print("MSE wiener:", mean_squared_error(slice_2d, wiener_denoised))
    print("PSNR wiener:", peak_signal_to_noise_ratio(slice_2d, wiener_denoised))
    show_images(
    [slice_2d, noisy_slice, mean_denoised, wiener_denoised],
    ["Original MRI", "Noisy MRI", "Mean Denoised", "Wiener Denoised"]
)



if __name__ == "__main__":
    main()
