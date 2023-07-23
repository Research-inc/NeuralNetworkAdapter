from common import Framework

class AdapterConfig:

	_framework = Framework.NotAvailable

	@classmethod
	def setFramework(cls, in_framework):
		cls._framework = in_framework
		print("\nselected Framework: ", in_framework.name)

	@classmethod
	def getFramework(cls):
		return cls._framework