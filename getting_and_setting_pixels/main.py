import cv2 as cv
import argparse
import sys

# Constructing an argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="newimage.jpg")
arg = vars(ap.parse_args())

# Loading the images and grabbing the spatial dimensions of those images
# And display the origin image to our screen
image = cv.imread(arg["image"])

if image is None:
    sys.exit("Could not load image")

(h, w) = image.shape[:2]
cv.imshow(arg["image"], image)

# images are simply numpy arrays -- with the origin (0,0) located at the top-left of the image
(b, g, r) = image[0, 0]
print(f"Pixel at (0,0) Red: {r} Green: {g} Blue: {b}")

# accessing pixel at x=50 y=20
(b, g, r) = image[20, 50]
print(f"Pixel at (50,20) Red: {r} Green: {g} Blue: {b}")

# Updating the pixel
image[20, 50] = (255, 0, 0)
(b, g, r) = image[20, 50]
(b, g, r) = image[20, 50]
print(f"Pixel at (50,20) Red: {r} Green: {g} Blue: {b}")

# --------------------------------------------- Image cropping -------------------------
# Getting the center pixel of the image
(cy, cx) = (h//2, w//2)

# Since we are using numpy array we can use array slicing to grab
# large chunk/region of interest from the image
# here we grap the top-left conner of the image
tl = image[0:cy, 0:cx]
cv.imshow("top left image", tl)

# in similar we can get all the four sides of the images using array slicing
br = image[cy:h, cx:w]
cv.imshow("bottom right", br)

tr = image[0:cy, cx:w]
cv.imshow("top right", tr)

bl = image[cy:h, 0:cx]
cv.imshow("bottom left", bl)
# ---------------------------------------------------------------------------------------

# Updating larger ranger of pixels
image[0:cy, 0:cx] = (0, 0, 255)
cv.imshow("Update", image)
cv.waitKey(0)