import yaml, json, sys
from pprint import pprint

with open("C:/Users/SC057441/Desktop/tokka/temp.yaml", 'r') as stream:
	data_yaml = yaml.load(stream)
with open('Age_category_Input.json', 'w') as outfile:
	json.dump(data_yaml, outfile)
	outfile.close()