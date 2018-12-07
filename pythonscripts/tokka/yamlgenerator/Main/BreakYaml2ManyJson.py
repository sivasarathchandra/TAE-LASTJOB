import yaml
import shutil
import os
import json
import time

i = count = temp = c = 0
d = temp2 = {}
lst = []
fstr = "C:/Users/SC057441/Desktop/Any/pythonscripts/tokka/yamlgenerator/Main/jsonfolder/temp1.txt"

if not os.path.exists(os.path.dirname(fstr)):
    os.makedirs(os.path.dirname(fstr))


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timeformat, end='')
        time.sleep(1)
        t -= 1
    print('\nwill delete the json folder now')
    if t == 0:
        print("entered to delete")
        shutil.rmtree('C:/Users/SC057441/Desktop/Any/pythonscripts/tokka/yamlgenerator/Main/jsonfolder')


def addTheDicToile(fstr):
    with open(fstr, 'r')as temp123:
        data = yaml.load(temp123)
        with open("C:/Users/SC057441/Desktop/Any/pythonscripts/tokka/yamlgenerator/Main/jsonfolder/" + lst[i] + ".json", 'w') as filename:
            print("the json are at : ", filename.name)
            final = json.dumps(data)
            filename.write(final)
        temp123.close()
        if i == 29:
            countdown(90)


with open("temp_final.yaml", 'r') as stream:
    for line in stream.readlines():
        if '---' in line:
            count = count + 1

while (temp < count):
    f = "temp" + str(temp)
    lst.append(f)
    temp = temp + 1
stream.close()
with open("temp_final.yaml", 'r') as stream1:
    for line in stream1.readlines():
        if not ('---') in line:
            with open('C:/Users/SC057441/Desktop/Any/pythonscripts/tokka/yamlgenerator/Main/jsonfolder/temp1.txt', 'a') as tempfile:
                tempfile.write(line)
        elif '---' in line and c > 1:
            addTheDicToile(fstr)
            i = i + 1
            with open('C:/Users/SC057441/Desktop/Any/pythonscripts/tokka/yamlgenerator/Main/jsonfolder/temp1.txt', 'w') as tempfile:
                tempfile.write("")
        c = c + 1
addTheDicToile(fstr)
i = count - 1
