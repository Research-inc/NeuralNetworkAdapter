from config import AdapterConfig
from common import Framework

def frameworkImport():
	_framework = AdapterConfig.getFramework()

	if _framework == Framework.Tensorflow:
		import tensorflow as tf
		print("Importing "+ _framework.name)		

	elif _framework == Framework.Pytorch:
		import torch
		print("Importing "+ _framework.name)
