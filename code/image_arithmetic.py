import sys
sys.path.append("/Users/udayanjoshi/opencv/build/lib")
import cv2
import numpy as np

x=raw_input("Enter image1: ")+(".jpg")
y=raw_input("Enter image2: ")+(".jpg")
img1=cv2.imread(x)
img2=cv2.imread(y)
cv2.imshow('Image1',img1)
cv2.waitKey(0)
cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.imshow('Image1+Image2',cv2.add(img1,img2))
cv2.waitKey(0)
cv2.imshow('Image1-Image2',cv2.subtract(img1,img2))
cv2.waitKey(0)
cv2.imshow('Image2-Image1',cv2.subtract(img2,img1))
cv2.waitKey(0)
cv2.destroyAllWindows()
