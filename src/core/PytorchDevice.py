import torch

class PytorchDevice:

	def __init__(self):

		print("Constructor PytorchDevice\n")


	def isGPUAvailable(self):		

		is_available = is_available = torch.cuda.is_available()
		return is_available
