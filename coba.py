import cv2
import numpy as np

def compare_mse(img1, img2):
  """Compares the mean squared error (MSE) between two images.

  Args:
    img1: The first image.
    img2: The second image.

  Returns:
    The MSE between the two images.
  """

  # Convert the images to grayscale.
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  # Calculate the MSE between the two images.
  mse = np.mean((img1 - img2) ** 2)

  return mse

img = cv2.imread('rahasia2.png')
img1 = cv2.imread('rahasia.png')
print(compare_mse(img1, img))