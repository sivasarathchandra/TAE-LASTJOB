import re

c = 0

with open("Account_23681835.txt") as fd:
    for line in fd.readlines():
        if 'partition:' in line:
            str = line.replace("bdb58e34-8ce5-432a-9946-329dd2a1a816","511d71b2-c065-4799-a0e4-7039086f95d3")
            with open("Account_23681835_up.txt",'a') as fd1:
                fd1.write(str)
            c = c+1
            print(str)
        else:
            with open("Account_23681835_up.txt",'a') as fd1:
                fd1.write(line)

print(c)
