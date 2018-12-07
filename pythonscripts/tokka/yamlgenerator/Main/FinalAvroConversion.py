import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json

lst = []
reader = DataFileReader(open("part-m-00000.avro", "rb"), DatumReader())  # no need to know the schema to read
for user in reader:
    print(type(user))
    lst.append(user)
    print(user)
with open('C:/Users/SC057441/Desktop/tokka/yamlgenerator/main/avrofinal2.json', 'a') as readfile:
    json.dump(lst,readfile,sort_keys=False, indent=4)
reader.close()