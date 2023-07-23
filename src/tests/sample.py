import sys
sys.path.append("../")

from common import Framework

from config import AdapterConfig

from core import Device

def testPytorch():

	AdapterConfig.setFramework(Framework.Pytorch)
	obj = Device()
	print("Is GPU Available: ", obj.isGPUAvailable())


def testTensorflow():

	AdapterConfig.setFramework(Framework.Tensorflow)
	obj = Device()
	print("Is GPU Available: ", obj.isGPUAvailable())



testPytorch()