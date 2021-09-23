# Comparing the intensities of two images
# Usage python --image1 *image* --image2 *image*
import cv2 as cv
import argparse
import imutils

# Construct an arg parser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True, help="path to first image")
ap.add_argument("-i2", "--image2", required=True, help="path to second image")
args = vars(ap.parse_args())

# initialise and empty list
intensities = []

# reading images to memory
# saving the images into a list
image1 = cv.imread(args["image1"])
image2 = cv.imread(args["image2"])
images = [image1, image2]


# function to save intensities of each image to a alist
# and also to resize the images to 300 x 300 pixels
# both images should have the same shape
def image_intensity(image_):

    # Resizing each image to a 300 x 300 pixels
    image_ = imutils.resize(image_, 300, 300, inter=cv.INTER_AREA)

    # initializing sum to zero
    sum_ = 0

    # grabbing the spatial dimension of the image
    # both the width and height
    h = image_.shape[0]
    w = image_.shape[1]

    # loop over the image pixel by pixel
    # sum each pixel and then adding it to
    # the initialized sum
    for y in range(0, h):
        for x in range(0, w):
            sum_ += sum(image_[y, x])

    # append the added intensities
    # to the already initialized list
    intensities.append(sum_)
    return intensities


# loop through the images in the images list
# and parsing every image to the image_intensity fucntion
for image in images:
    image_intensity(image)

# Using the intensities to decide the image which is really bright
# and using the if elif statement to determine the one with the highest intensities
# to show the image
if intensities[0] > intensities[1]:
    cv.imshow(args["image1"], image1)
elif intensities[0] == intensities[1]:
    cv.imshow(args["image1"], image1)
    cv.imshow(args["image2"], image2)
    print("Both images have the same intensities")
else:
    cv.imshow(args["image2"], image2)
cv.waitKey(0)
