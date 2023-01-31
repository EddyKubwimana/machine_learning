import matplotlib.pyplot as plt
import tensorflow as tf
import random
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35])
y=np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35])
model=tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1,input_shape=[1]))
model.compile(optimizer=tf.keras.optimizers.Adam(0.1),
              loss='mean_squared_error',
              metrics=['accuracy'])
history=model.fit(x,y, epochs=2000)
Predict=model.predict([10])
print(Predict)
