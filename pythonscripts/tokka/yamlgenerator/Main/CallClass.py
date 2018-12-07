import AllClassFiles

cobj = AllClassFiles.AllConversions()
print("Changing the partition ID before actual stuff starts")
cobj.beforeConversion()
print("Entering accounts")
cobj.AccountsConvertion()
print("Entering financials")
cobj.FinacialConversion()
print("Removing lines from Yaml")
cobj.RemoveExtraFromYaml()