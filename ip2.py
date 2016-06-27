import sys
sys.path.append("/Users/udayanjoshi/opencv/build/lib")
# import the necessary packages
from pyimagesearch.transform import four_point_transform
import numpy as np
import cv2

# construct the argument parse and parse the arguments


# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
x=raw_input("Enter image name: ")
image = cv2.imread(x+".jpg")
pts = np.array(, dtype = "float32")

# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)

# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)