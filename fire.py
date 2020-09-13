
from tensorflow.python.keras.models import Sequential
import tensorflow.compat.v1 as tf1
tf1.disable_v2_behavior()
from tensorflow.python.keras.layers import Dense,Dropout,Activation
from tensorflow.python.keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.models import load_model
from collections import deque
from sklearn.preprocessing import LabelBinarizer
import cv2
classifier=Sequential()
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation = "relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(32,3,3,activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(128,activation='relu'))
classifier.add(Dense(1,activation='sigmoid'))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen=ImageDataGenerator(rescale=1./255)


training_set=train_datagen.flow_from_directory("C:\\Users\\Deeksha Priya\\Desktop\\image_data\\training_set",target_size=(64,64),batch_size=32,class_mode='binary')
test_set=test_datagen.flow_from_directory("C:\\Users\\Deeksha Priya\\Desktop\\image_data\\test_set",target_size=(64,64),batch_size=32,class_mode='binary')
classifier.fit_generator(training_set,steps_per_epoch=600,epochs=1,validation_data=test_set,validation_steps=94)
classifier.save("model.h5")

