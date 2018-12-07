import yaml, json, sys
from pprint import pprint

with open("C:/Users/SC057441/Desktop/tokka/funk.yaml", 'r') as stream:
	data_yaml = yaml.load(stream)
	#print(data_yaml)
with open('C:/Users/SC057441/Desktop/tokka/data1.json', 'w') as outfile:
	json = json.dumps(data_yaml)
	#print(json)
	outfile.write(json)
	outfile.close()
