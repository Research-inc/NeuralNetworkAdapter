from enum import Enum

# Enumeration to identify the type of framework used underneath
class Framework(Enum):
	NotAvailable	= 0
	Pytorch 		= 1
	Tensorflow		= 2

# Enumeration to identify the type of device beneath
class DeviceType(Enum):
	GPU 	= 	1
	MPS		= 	2
	CPU		=	3


