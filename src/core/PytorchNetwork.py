import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


# class NeuralNetwork(nn.Module):
#     def __init__(self):
        
#         self.flatten = nn.Flatten()
#         self.linear_relu_stack = nn.Sequential(
#             nn.Linear(28*28, 512),
#             nn.ReLU(),
#             nn.Linear(512, 512),
#             nn.ReLU(),
#             nn.Linear(512, 10),
#         )

#     def forward(self, x):
#         x = self.flatten(x)
#         logits = self.linear_relu_stack(x)
#         return logits


class PytorchNetwork(nn.Module):

	def __init__(self, in_config):

		super().__init__()
		print("Constructor PytorchNetwork\n")

		num_outer_layers = len(in_config)		

		outer_layers = []

		for outer_layer in in_config:
			inner_layers = []
			if "nested" in outer_layer:			
				for inner_layer in outer_layer["nested"]:
					if inner_layer['layer'] == 'linear':
						inner_layers.append(nn.Linear(inner_layer["in_features"], inner_layer["out_features"]))
					elif inner_layer['layer']=='relu' :
						inner_layers.append(nn.ReLU())					

			if outer_layer['layer']=='flatten' :
				outer_layers.append(nn.Flatten())
			elif outer_layer['layer']=='relu' :
				outer_layers.append(nn.ReLU())
			elif outer_layer['layer']=='sequential':
				if len(inner_layers):
					outer_layers.append(nn.Sequential(*inner_layers))							

		print(outer_layers)
		self._layers = outer_layers

	def forward(self, x):

		for layer in self._layers:
			x = layer(x)

		return x










	