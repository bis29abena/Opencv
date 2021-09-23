import cv2 as cv
import numpy as np
import argparse

# construct an argparse to parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="path to input image")
args = vars(ap.parse_args())

# loading the image and displaying it on the screen
image = cv.imread(args["image"])
cv.imshow("original", image)

# we split the channels of the image
# cv use the B,G,R color combination but not R,G,B
(B, G, R) = cv.split(image)
cv.imshow("Blue", B)
cv.imshow("Green", G)
cv.imshow("Red", R)

# merging the images
merged = cv.merge([B, G, R])
cv.imshow("Merged", merged)
cv.INTER_BI
cv.waitKey(0)