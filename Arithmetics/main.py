import cv2 as cv
import numpy as np
import argparse
import imutils

# Constructing the argument parser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to input file", type=str, default="flower.jpg")
args = vars(ap.parse_args())

# Loading the image and displaying it on the screen]
# Resizing the images 300 x 300
image = cv.imread(args["image"])
image = imutils.resize(image, 300, 300, cv.INTER_AREA)
cv.imshow("Original", image)
cv.imwrite("Original.jpg", image)

# images are numpy arrays stored as unsigned 8bit integers
# with values in the range off [0-255]: when using the add/subtract
# fxn in opencv, these values will be clipped to these to this range
# even if they fall outside range after applying the
added = cv.add(np.uint8([200]), np.uint8([100]))
subtract = cv.subtract(np.uint8([50]), np.uint8([100]))
print(f"max of 255: {added}")
print(f"min of 0: {subtract}")

# Using numpy arithmetic operations rather than opencv operations
# will result to in a modulo wrap around instead of being clipped
# to the range of [0-255]
added = np.uint8([200]) + np.uint8([100])
subtract = np.uint8([50]) - np.uint8([100])
print(f"max of 255: {added}")
print(f"min of 0: {subtract}")

# Increasing the intensity of the input image by 100 is
# accomplished by constructing a Numpy array that has the same
# dimensions as the input image, filling it with ones and multiplying
# it by 100 and then adding the iput image to the matrix together
M = np.ones(image.shape, dtype="uint8") * 100
added = cv.add(image, M)
cv.imshow("Lighter", added)
cv.imwrite("lighter.jpg", added)

# Similarly we can subtract 50 pixels from our images and make it
# darker
M = np.ones(image.shape, dtype="uint8") * 50
subtract = cv.subtract(image, M)
cv.imshow("darker", subtract)
cv.imwrite("darker.jpg", subtract)

cv.waitKey(0)