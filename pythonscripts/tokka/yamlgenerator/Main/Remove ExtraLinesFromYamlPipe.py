import yaml
import pprint


with open("yamldata21.yaml",'r') as yamlfile:
    for line in yamlfile.readlines():
        if "---" in line:
            with open("accounts21.yaml",'a') as lastyml1:
                lastyml1.write('---')
                lastyml1.write('\n')
                continue
        #print(line)
        if "lastUpdate" in line:
            #print("enterinig if")
            str = line.splitlines()
            continue
        elif "codes:" in line:
            #print("entering the codes if")
            str = line.splitlines()
            continue
        else:
            with open("accounts21.yaml",'a') as lastyml:
                lastyml.write(line)
                print("Wrote into a file with the name :  ", lastyml.name)
#lastyml.close()