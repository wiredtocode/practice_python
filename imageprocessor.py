import numpy as np

import matplotlib.pyplot as plt 

img = plt.imread('C:\\Users\\armin\\Desktop\\whatevr\\image.jpg')


print(f"Image Type: {type(img)}")
print(f"Image Shape (Height, Width, Channels): {img.shape}")
print(f"Data Type of Pixels: {img.dtype}")


def crop_image(image, start_row, end_row, start_col, end_col):
    """
    Uses NumPy slicing to crop a specific region of the image.
    """
    return image[start_row:end_row, start_col:end_col].copy()



# greyscale simplifies image processing by reducing complex three-channel (RGB) data into a single-channel intensity map. 

my_pixel = img[100, 150]





print("The pixel data is:", my_pixel)