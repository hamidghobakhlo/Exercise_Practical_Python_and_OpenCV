from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser(description="ArgumentParser")
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0)- Red: {}, Green: {}, Blue: {}".format(r,
g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0)- Red: {}, Green: {}, Blue: {}".format(r,
g, b))

cv2.waitKey(0)
# python 2_getting_and_setting.py --i images/trex.png
