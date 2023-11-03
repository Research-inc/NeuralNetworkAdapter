import tensorflow as tf

class TensorflowNetwork():

	def __init__(self, in_config):

		super().__init__()
		print("Constructor TensorflowNetwork\n")

		num_outer_layers = len(in_config)
		
		outer_layers = []

		for outer_layer in in_config:
			inner_layers = []
			if "nested" in outer_layer:			
				for inner_layer in outer_layer["nested"]:
					if inner_layer['layer'] == 'linear':
						inner_layers.append(tf.keras.layers.Dense(inner_layer["in_features"], activation='linear'))
						#inner_layers.append(nn.Linear(inner_layer["in_features"], inner_layer["out_features"]))
					elif inner_layer['layer']=='relu' :
						inner_layers.append(tf.keras.layers.ReLU())		

			if outer_layer['layer']=='flatten' :
				outer_layers.append(tf.keras.layers.Flatten())
			elif outer_layer['layer']=='relu' :
				outer_layers.append(tf.keras.layers.ReLU())
			elif outer_layer['layer']=='sequential':
				if len(inner_layers):
					outer_layers.append(tf.keras.Sequential(inner_layers))							

		print(outer_layers)
		self._layers = tf.keras.Sequential(outer_layers)


