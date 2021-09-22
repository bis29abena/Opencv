import cv2 as cv
import argparse
import imutils

# construct the argparse taking the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="path to input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)

# Cropping the face using array slicing
face = image[95:250, 100:225]
cv.imshow("face", face)

# Cropping the body
body = image[240:440, 20:280]
cv.imshow("body", body)

# Croping the people at the back and maximizing the image
people = image[165:230, 0:80]
max_people_image = imutils.resize(people, 300, 300, inter=cv.INTER_LANCZOS4)
cv.imshow("people at back", max_people_image)

cv.waitKey(0)