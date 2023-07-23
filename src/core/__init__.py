from .device import Device

from config import AdapterConfig
from common import Framework

framework = AdapterConfig.getFramework()

#if framework == Framework.Tensorflow:
	#from .TensorflowDevice import TensorflowDevice
	#print("\nImporting TensorflowDevice")

#elif framework == Framework.Pytorch:
#	from .PytorchDevice import PytorchDevice
#	print("\nImporting PytorchDevice")
