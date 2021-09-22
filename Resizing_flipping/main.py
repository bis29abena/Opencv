import cv2 as cv
import argparse
import imutils

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="30th_birthday.png")
args = vars(ap.parse_args())

# load the original input image and display it on our screen
image = cv.imread(args["image"])
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")
cv.imshow("Original", image)

# lets resize our image to 300pixels wide but
# first we need to define aspect ratio to prevent skewness/distortion
# first calculate the ratios by using the new width to the old width
r = 300.0 / w
dim = (300, int(h * r))

# perform the actual resizing of the image
resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
(h, w) = resized.shape[:2]
print(f"height: {h}, width: {w}")
cv.imshow("Resized (width)", resized)

# lets resize our image to tallpixels tall but
# first we need to define aspect ratio to prevent skewness/distortion
# first calculate the ratios by using the new height to the old height
r = 150.0 / h
dim = (int(w * r), 150)

# perform the actual resizing of the image
resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
(h, w) = resized.shape[:2]
print(f"height: {h}, width: {w}")
cv.imshow("Resized (height)", resized)

# Resizing via imutils no need for an aspect ratio
# because this functions maintains it which prevents skewness/distortion
resized = imutils.resize(image, width=300, height=300)
cv.imshow("Resized via imutils", resized)

# Construct a list of interpolation methods by cv
methods = [
    ("cv.INTER_NEAREST", cv.INTER_NEAREST),
    ("cv.INTER_LINEAR", cv.INTER_LINEAR),
    ("cv.INTER_AREA", cv.INTER_AREA),
    ("cv.INTER_CUBIC", cv.INTER_CUBIC),
    ("cv.INTER_LANCZOS4", cv.INTER_LANCZOS4)
]

for (name, method) in methods:
    # Increase the size of an image by 3x
    # Using the current interpolation method
    print(f"[INFO] {name}")
    resized = imutils.resize(image, w * 3, inter=method)
    cv.imshow(f"Method: {name}", resized)
    cv.waitKey(0)
    
cv.waitKey(0)