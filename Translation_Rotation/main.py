import cv2 as cv
import argparse
import numpy as np
import imutils

# construct the argument parser and the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv.png", help="path to the input image")
args = vars(ap.parse_args())

# loading the image to memory and displaying it on the screen
image = cv.imread(args["image"])
(h, w, c) = image.shape
cv.imshow("Output", image)

# Shifting the image 25pixels to the right and 50pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted_image = cv.warpAffine(image, M, (w, h))
cv.imshow("Shifted right down", shifted_image)

# Shifting the image 50pixels to the left and 90 pixels up
# here we specify negative numbers
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted_image = cv.warpAffine(image, M, (w, h))
cv.imshow("Shifted left up", shifted_image)

# using imutils helper functions to translate images
shifted = imutils.translate(image, -50, -90)
cv.imshow("Shifted", shifted)
cv.waitKey(0)
