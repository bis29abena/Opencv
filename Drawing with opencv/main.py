import numpy as np
import cv2 as cv

# initializing our canvas by 300x300 pixels image with 3 channels
# (Red, Green, Blue) with a black background
canvas = np.ones((300, 300, 3), dtype="uint8")

# Drawing a greenline from the top left to the bottom right corner of the canvas
green = (0, 255, 0)
cv.line(canvas, (0, 0), (300, 300), green, thickness=1 )
cv.imshow("Canvas", canvas)
cv.waitKey(0)

# Draw a 3 pixel thick red line from the top right corner to the bottom left
red = (0, 0, 255)
cv.line(canvas, (0, 300), (300, 0), red, 3)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

# Draw a green 50 x 50 pixel square, starting at 10x10 and ending at 60x60
cv.rectangle(canvas, (10, 10), (60, 60), green, 2)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

# draw another rectangle, this one red with 5 pixel thickness
cv.rectangle(canvas, (50, 200), (200, 255), red, 5)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

# draw a final rectangle (blue and filled in)
Blue = (255, 0, 0)
cv.rectangle(canvas, (200, 50), (255, 125), Blue, -1)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

# Re-initializing the canvas as an empty arrat
# And computing the center of the canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(cY, cX) = (canvas.shape[0]//2, canvas.shape[1]//2)
white = (255, 255, 255)

# loop over increasing radii, from 25 pixels to 150 pixels in 25
# pixel increment
for r in range(5, 175, 25):
    cv.circle(canvas, (cX, cY), r, white)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

# let's draw 25 random circles
for i in range(0, 25):
    # Randomly generating radius size from 5 to 200
    radius = np.random.randint(low=5, high=200)

    # Randomly selecting colors
    color = np.random.randint(low=0, high=256, size=3).tolist()

    # Radomly selecting center of the points
    pt = np.random.randint(low=0, high=300, size=2)

    # Drawing the circle
    cv.circle(canvas, tuple(pt), radius, color, -1)

cv.imshow("Canvas", canvas)
cv.waitKey(0)