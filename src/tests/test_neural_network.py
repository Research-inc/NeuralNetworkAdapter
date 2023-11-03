import sys
sys.path.append("../")

from common import Framework

from config import AdapterConfig

from core import Device
from core import Network

from collections import OrderedDict

def test_pytorch_network():
	AdapterConfig.setFramework(Framework.Pytorch)		

	net_config = [
						{
						'layer': 'flatten'
						}, 
						
						{
						'layer': 'sequential', 
						'nested' :[
									{
										'layer':'linear', 
										'in_features':784,
										'out_features':512
									},
									{
										'layer':'relu'
									},
									{
										'layer':'linear', 
										'in_features':512,
										'out_features':512
									},
									{
										'layer':'relu'
									},
									{
										'layer':'linear', 
										'in_features':512,
										'out_features':10
									}									
								] 
						}
				]

	obj = Network(net_config)

	print("Configured Network")
	print(obj.getNetworkConfig())


def test_tensorflow_network():
	AdapterConfig.setFramework(Framework.Tensorflow)		

	net_config = [
						{
						'layer': 'flatten'
						}, 
						
						{
						'layer': 'sequential', 
						'nested' :[
									{
										'layer':'linear', 
										'in_features':784,
										'out_features':512
									},
									{
										'layer':'relu'
									},
									{
										'layer':'linear', 
										'in_features':512,
										'out_features':512
									},
									{
										'layer':'relu'
									},
									{
										'layer':'linear', 
										'in_features':512,
										'out_features':10
									}									
								] 
						}
				]

	obj = Network(net_config)

	print("Configured Network")
	print(obj.getNetworkConfig())



test_tensorflow_network()
