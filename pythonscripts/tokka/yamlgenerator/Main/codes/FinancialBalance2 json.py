import json
import pprint

finalJson = {}
recorddict = {"dataPartitionId": "511d71b2-c065-4799-a0e4-7039086f95d3", "financialBalanceId": "23577834"}

finalJson['recordId'] = recorddict
with open("Financial_Balance2.txt") as fd:
    for line in fd.readlines():
        if not line.strip():
            continue
        else:
            if line.startswith("{"):
                value = json.loads(line)
                finalJson[key1].append(value)
            else:
                key = line.split(":")[0]
                if key == "financial_balance record":
                    key1 = key.replace("financial_balance record", "financialBalances")
                elif key == "charge record":
                    key1 = key.replace("charge record", "charges")
                if key1 not in finalJson.keys():
                    finalJson[key1] = []

pprint.pprint(finalJson)
with open("Financial_Balance2.json",'w')as jsonwrite:
    json.dump(finalJson,jsonwrite,sort_keys=False)
    print("Wrote in the file : ", jsonwrite.name)
    jsonwrite.close()