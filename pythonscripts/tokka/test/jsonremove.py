import json

with open("C:/Users/SC057441/Desktop/tokka/test.json", 'r', encoding='UTF-8') as stream:
	data = json.dumps(stream,)
	print(data)
#with open("C:/Users/SC057441/Desktop/tokka/test1251/Denial/person.json", 'w') as outfile:
#	final = json.dumps(data)
#	outfile.write(final)
#	outfile.close()
