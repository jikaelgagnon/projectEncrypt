from imutils.contours import sort_contours
import numpy as np
import pytesseract
import argparse
import imutils
import sys
import cv2


# this part of the code requires an argument of the form --image to be passed in the command line
# the image is then passed in the variable args

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())

# cv2(Opencv command reads the image path and returns the image)
image = cv2.imread(args["image"])
# Opencv command converts image from its corrent format to grayscale(easier to read)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# finds the height and width of the image in (if I understand the documentation properly pixels e.g. example H=2956, W=2006)
(H, W) = gray.shape