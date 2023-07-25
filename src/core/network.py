from common import *
from config import *


class Network:

	def __init__(self, in_config):

		self._framework = AdapterConfig.getFramework()
		self.setNetworkConfig(in_config)
		if self._framework == Framework.Tensorflow:
			from .TensorflowNetwork import TensorflowNetwork
			frameworkImport()
			self._device = TensorflowNetwork(self._config)

		elif self._framework == Framework.Pytorch:
			from .PytorchNetwork import PytorchNetwork
			frameworkImport()
			self._device = PytorchNetwork(self._config)


	def setNetworkConfig(self, in_config):

		self._config = in_config


	def getNetworkConfig(self):

		return self._config