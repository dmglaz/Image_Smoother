import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
# import functions
from functions import *

folder_path = "Dirty_Images\\"
dirty_pics = {1: "1.png",2: "2.jpg"}

convolution_2D_filter(folder_path+dirty_pics[2], 3)
averaging_smoother(folder_path+dirty_pics[2])
gaussian_smoother(folder_path+dirty_pics[2])
median_smoother(folder_path+dirty_pics[2])
