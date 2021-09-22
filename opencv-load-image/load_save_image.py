import argparse
import cv2 as cv
import sys
# python load_image_opencv.py --image 30th_birthday.png --save new_image

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="requires an input image")
ap.add_argument("-s", "--save", required=True, help="requires a path to save image to")
args = vars(ap.parse_args())

save_image = args["save"]

# load the image from disk via "cv2.imread" and then grab the spatial
image = cv.imread(args["image"])

# If image is not found exit from the program
if image is None:
    sys.exit("Could not read image")

# dimensions, including width, height, and number of channels
# display the image width, height, and number of channels to our
# terminal
(h, w, c) = image.shape[:3]
print(f"height is {h} width is {w} channels are {c}")

# show the image and wait for a keypress
cv.imshow(save_image, image)
cv.waitKey(0)

# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
cv.imwrite(f"{save_image}.jpg", img=image)
