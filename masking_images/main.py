import cv2 as cv
import numpy as np
import argparse

# constructing argparse to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="path to input image")
args = vars(ap.parse_args())

# loading the image and displaying it on a screen
image = cv.imread(args["image"])
cv.imshow("original", image)

# a mask has the same size of our image but has only two pixel
# value that's 0 and 255-- pixels with a value of zero(background) are ignored
# in the original image while mask pixels with a value of 255 are to be kept
# in the original image.
mask = np.zeros(image.shape[:2], dtype="uint8")
cv.rectangle(mask, (30, 85), (326, 430), 255, -1)
cv.imshow("mask_rectangle", mask)

# applying our mask: notice how our image will be cropped out
masked = cv.bitwise_and(image, image, mask=mask)
cv.imshow("cropped image", masked)

# masking to crop out the face only
# here we draw a circle with a mask on
mask = np.zeros(image.shape[:2], dtype="uint8")
cv.circle(mask, (170, 194), 100, 255, -1)
cv.imshow("circular mask", mask)

masked = cv.bitwise_and(image, image, mask=mask)

cv.imshow("crooped face", masked)
cv.waitKey(0)