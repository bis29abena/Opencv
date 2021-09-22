import cv2 as cv
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv.png", help="Path to input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("output", image)

# Grabbing the spatial dimension of the image and calculating the center
(h, w, c) = image.shape
(cX, cY) = (w//2, h//2)

# Rotate your image about 45 degrees anti clockwise around the center of your image
M = cv.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("rotated by 45 degree anticlock wise", rotated)

# Rotate your image about 45 degrees clockwise around the center of your image
M = cv.getRotationMatrix2D((cX, cY), -45, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("rotated by 45 degree clock wise", rotated)


# Rotate your image about 90 degrees anti clockwise around the center of your image
M = cv.getRotationMatrix2D((cX, cY), 90, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("rotated by 90 degree anticlock wise", rotated)

# Rotate your image about 90 degrees clockwise around the center of your image
M = cv.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("rotated by 90 degree clock wise", rotated)

# Rotate with imutils
rotated = imutils.rotate(image, 180)
cv.imshow("Rotated using imutils at 180 degrees", rotated)

# Rotating the image by the 33 degrees ensuring that
# the image stays around the view area
rotated = imutils.rotate_bound(image, -33)
cv.imshow("rotated within the boundaries", rotated)

cv.waitKey(0)