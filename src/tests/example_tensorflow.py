import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')

print(type(gpus))