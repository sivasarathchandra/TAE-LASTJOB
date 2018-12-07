import yaml

with open("C:/Users/SC057441/Desktop/tokka/temp.yaml", 'r') as stream:
	data = yaml.load(stream)
with open("C:/Users/SC057441/Desktop/tokka/final.json", 'r') as outfile:
	final = jason.dumps(outfile)
	print("List of main keys from Yaml: ")
	for k,v in data.items():
		print(k)
	Key_Iter = input("Enter Key from the above list ")
	New_Key = input("New Key: ")
	New_Value = input("New Value: ")
	d = {New_Key : New_Value}
	for k,v in data.items():
		#print(k)
		#print("Length of value is ", len(v))
		#print("Passing one key by key")
		if k == Key_Iter:
			if k == "recordId":
				data[Key_Iter][New_Key] = New_Value
			if k == "accounts":
				data[k].append(d)
			if k == "transactions":
				data[k].append(d)
with open("C:/Users/SC057441/Desktop/tokka/finaldata.yaml", 'w') as outfile:
	yaml.dump(data,outfile,default_flow_style=False)
	outfile.close()
print("Updated in the FinalData.yaml file.")
