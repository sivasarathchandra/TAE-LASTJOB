import yaml
import json

with open("accounts.json", 'r') as stream:
	data = yaml.load(stream)
with open("yamldata.yaml", 'w') as outfile:
	final = json.dumps(data)
	outfile.write(final)
	outfile.close()
