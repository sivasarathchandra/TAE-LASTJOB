import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json

schema = avro.schema.Parse(open("user.avsc","rb").read())  # need to know the schema to write

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()
lst = []
dict = {
}
reader = DataFileReader(open("users.avro", "rb"), DatumReader())  # no need to know the schema to read
for user in reader:
    print(type(user))
    lst.append(user)
    print(user)
with open('C:/Users/SC057441/Desktop/tokka/avrofinal.json', 'w') as readfile:
    json.dump(lst,readfile,sort_keys=True, indent=4)
    #readfile.write('{')
    #readfile.write('\n')
    #for l in lst:
     #   json.dump(l,readfile,sort_keys=True, indent=4)
      #  readfile.write(',')
       # readfile.write('\n')
    #readfile.write('}')
reader.close()