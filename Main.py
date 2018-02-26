import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
# import functions
from functions import *


folder_path = "Dirty_Images\\"
dirty_pics = {1: "1.png",2: "2.jpg"}

kernel = {
    "sharpen": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]),
    "edge_dtct1": np.array([[1,0,-1],[0,0,0],[-1,0,1]]),
    "edge_dtct2": np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]]),
    "edge_dtct1": np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
    "edge_enhance": np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]]),
    "average": np.ones((3, 3), np.float32) / pow(3,2),
    "gauss_blur33": np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/16,
    "gauss_blur55": np.array([[1, 4,6,4, 1], [ 4, 16, 24, 16,  4], [ 6, 24, 36, 24,  6], [ 4, 16, 24, 16,  4],[1, 4,6,4, 1] ]) / 256,
    "unsharp_masking55": np.array([[1, 4,6,4, 1], [ 4, 16, 24, 16,  4], [ 6, 24, -476, 24,  6], [ 4, 16, 24, 16,  4],[1, 4,6,4, 1]])* (-1/256)
}

img = cv2.imread(folder_path+dirty_pics[2])
new_img = convolution_2D_filter(img, kernel["gauss_blur33"])
img2 = convolution_2D_filter(new_img, kernel["edge_dtct1"])



averaging_smoother(folder_path+dirty_pics[2])
# gaussian_smoother(folder_path+dirty_pics[2])
# median_smoother(folder_path+dirty_pics[2])
