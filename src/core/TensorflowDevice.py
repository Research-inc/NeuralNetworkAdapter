import tensorflow as tf

class TensorflowDevice:

	def __init__(self):

		print("Constructor TensorflowDevice\n")

	def isGPUAvailable(self):
		gpus = tf.config.list_physical_devices('GPU')
		is_available = (len(gpus)!=0)
		return is_available
