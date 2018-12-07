import json
import yaml
import time

class AllConversions(object):

    def beforeConversion(self):
        c=0
        with open("Account_23681835.txt") as fd:
            for line in fd.readlines():
                if 'partition:' in line:
                    str = line.replace("bdb58e34-8ce5-432a-9946-329dd2a1a816", "511d71b2-c065-4799-a0e4-7039086f95d3")
                    with open("Account_23681835_up.txt", 'a') as fd1:
                        fd1.write(str)
                    c = c + 1
                    #print(str)
                else:
                    with open("Account_23681835_up.txt", 'a') as fd1:
                        fd1.write(line)

    def AccountsConvertion(self):
        finalJson = {}
        dataPartitionId = '511d71b2-c065-4799-a0e4-7039086f95d3'
        accountId = 23577834
        key1 = None
        recorddict = {"dataPartitionId": dataPartitionId, "accountId": accountId}

        finalJson['recordId'] = recorddict
        with open("Account_23681835_up.txt") as fd:
            for line in fd.readlines():
                if not line.strip():
                    continue
                else:
                    if line.startswith("{"):
                        value = json.loads(line)
                        finalJson[key1].append(value)
                    else:
                        key = line.split(":")[0]
                        if key == "account record":
                            key1 = key.replace("account record", "accounts")
                            # print(key1)
                        elif key == "transaction record":
                            key1 = key.replace("transaction record", "transactions")
                        if key1 not in finalJson.keys():
                            finalJson[key1] = []

        # pprint.pprint(finalJson)
        with open("Account_23681835.json", 'w')as jsonwrite:
            json.dump(finalJson, jsonwrite, sort_keys=False)
            print("Wrote in the file : ", jsonwrite.name)
            jsonwrite.close()

    def FinacialConversion(self):
        finalJson = {}
        dataPartitionId = '511d71b2-c065-4799-a0e4-7039086f95d3'
        financialBalanceId = 23577834
        key1 = None
        recorddict = {"dataPartitionId": dataPartitionId, "financialBalanceId": financialBalanceId}

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

        #pprint.pprint(finalJson)
        with open("Financial_Balance2.json", 'w')as jsonwrite:
            json.dump(finalJson, jsonwrite, sort_keys=False)
            print("Wrote in the file : ", jsonwrite.name)
            jsonwrite.close()

    def RemoveExtraFromYaml(self):
        start = time.clock()
        with open("Account_23681835.yaml", 'r') as yamlfile:
            for line in yamlfile.readlines():
                if "---" in line:
                    with open("Account_236818354.yaml", 'a') as lastyml1:
                        lastyml1.write('---')
                        lastyml1.write('\n')
                        continue
                # print(line)
                if "lastUpdate" in line:
                    str = line.splitlines()
                    continue
                elif "codes:" in line:
                    str = line.splitlines()
                    continue
                else:
                    with open("Account_236818354.yaml", 'a') as lastyml:
                        lastyml.write(line)
        print(time.clock() - start)
        print("Done!")