import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2


# 2D Convolution ( Image Filtering )
def convolution_2D_filter(img, kernel):
    return cv2.filter2D(img, -1, kernel)

def show_2_images(org_img,new_img):
    plt.subplot(121), plt.imshow(org_img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(new_img), plt.title('New')
    plt.xticks([]), plt.yticks([])
    plt.show()

# Image Blurring (Image Smoothing) - convolving the image with a low-pass filter kernel


# 1.Averaging
def averaging_smoother(path):

    img = cv2.imread(path)

    blur = cv2.blur(img, (5, 5))

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 2.Gaussian Filtering
def gaussian_smoother(path):
    img = cv2.imread(path)
    blur = cv2.GaussianBlur(img,(5,5),0)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Gaussian Filtering')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 3.Median Filtering
def median_smoother(path):
    img = cv2.imread(path)
    blur = cv2.medianBlur(img, 5)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Median Filtering')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 4.Bilateral Filtering
def bilateral_smoother(path):
    img = cv2.imread(path)

    blur = cv2.bilateralFilter(img,9,75,75)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Bilateral Filtering')
    plt.xticks([]), plt.yticks([])
    plt.show()

