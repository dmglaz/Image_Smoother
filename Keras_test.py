from keras.layers import Convolution2D, MaxPooling2D, Activation
from keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

cat = cv2.imread('Images\\cat.png')

# here we get rid of that added dimension and plot the image
def visualize_cat(model, cat):
    # Keras expects batches of images, so we have to add a dimension to trick it into being nice
    cat_batch = np.expand_dims(cat,axis=0)
    conv_cat = model.predict(cat_batch)
    conv_cat = np.squeeze(conv_cat, axis=0)
    print (conv_cat.shape)
    plt.imshow(conv_cat)

model = Sequential()
model.add(Convolution2D(3,    # number of filter layers
                        (3,    # y dimension of kernel (we're going for a 3x3 kernel)
                        3),    # x dimension of kernel
                        input_shape=cat.shape))
# Keras expects batches of images, so we have to add a dimension to trick it into being nice
cat_batch = np.expand_dims(cat,axis=0)
conv_cat = model.predict(cat_batch)
visualize_cat(model, cat)