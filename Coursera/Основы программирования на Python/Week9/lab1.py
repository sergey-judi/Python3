import tensorflow as tf
import numpy as np


model = tf.keras.Sequential([tf.keras.layers.Flatten(),
                             tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xValues = np.array([-1, 0, 1, 2, 3, 4, 5, 6], dtype=int)
yValues = np.array([-2, 1, 4, 7, 10, 13, 16, 19], dtype=int)

model.fit(xValues, yValues, epochs=500)

print(*model.predict([30, 40]))