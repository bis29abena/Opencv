import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv.png", help="path to input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

# Flipping the image horizontally
flip = cv.flip(image, 1)
cv.imshow("flipped horizontally", flip)

# Flipping the image vertically
flip = cv.flip(image, 0)
cv.imshow("flipping vertically", flip)
cv.waitKey(0)
