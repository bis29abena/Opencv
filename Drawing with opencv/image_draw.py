import argparse
import cv2 as cv
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png")
arg = vars(ap.parse_args())

image = cv.imread(arg["image"])

if image is None:
    sys.exit("Could not load image")

# Drawing circle around the face
cv.circle(image, (165, 195), 90, (0, 0, 255), 2)
# Drawing filled circles on the eyes
cv.circle(image, (150, 165), 15, (0, 255, 0), -1)
cv.circle(image, (190, 175), 15, (0, 255, 0), -1)
# Drawing a rectangle on the mouth
cv.rectangle(image, (140, 195), (185, 230), (255, 0, 0), 2)

cv.imshow(arg["image"], image)
cv.waitKey()