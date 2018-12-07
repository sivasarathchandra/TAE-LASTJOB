import json
import pprint

finalJson = {}
dataPartitionId = '511d71b2-c065-4799-a0e4-7039086f95d3'
accountId = 23577834
key1 = None
recorddict = {"dataPartitionId": dataPartitionId, "accountId": accountId}

finalJson['recordId']=recorddict
with open("accounts.txt") as fd:
    for line in fd.readlines():
        if not line.strip():
            continue
        else:
            if line.startswith("{"):
                value = json.loads(line)
                finalJson[key1].append(value)
            else:
                key = line.split(":")[0]
                if key =="account record":
                    key1 = key.replace("account record","accounts")
                    #print(key1)
                elif key == "transaction record":
                    key1 = key.replace("transaction record","transactions")
                if key1 not in finalJson.keys():
                    finalJson[key1] = []

#pprint.pprint(finalJson)
with open("accounts.json",'w')as jsonwrite:
    json.dump(finalJson,jsonwrite,sort_keys=False)
    print("Wrote in the file : ", jsonwrite.name)
    jsonwrite.close()
