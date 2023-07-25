from common import *
from config import *


class Device:

	_device = None
	def __init__(self):

		self._framework = AdapterConfig.getFramework()

		if self._framework == Framework.Tensorflow:
			from .TensorflowDevice import TensorflowDevice
			frameworkImport()
			self._device = TensorflowDevice()

		elif self._framework == Framework.Pytorch:
			from .PytorchDevice import PytorchDevice
			frameworkImport()
			self._device = PytorchDevice()
		
	def isGPUAvailable(self):		

		return self._device.isGPUAvailable()
