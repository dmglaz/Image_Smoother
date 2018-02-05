import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

dirty_pics = {1: "1.png",2: "2.jpg"}

img = cv2.imread('Dirty_Images\\'+dirty_pics[2])

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
