from PIL import Image
import numpy as np


def compare_images(image_path1, image_path2):
    # Open image
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Convert the image to a numpy array
    img1_array = np.array(img1)
    img2_array = np.array(img2)

    # Calculate the difference (mean square error) between two images
    diff = np.sum((img1_array.astype("float") - img2_array.astype("float")) ** 2)
    n_diff = diff / float(img1_array.shape[0] * img1_array.shape[1])
    mse = np.sqrt(n_diff)

    return mse


# Using functions
mse = compare_images("a1.jpg", "a2.jpg")
print(f"Mean Squared Error: {mse}")