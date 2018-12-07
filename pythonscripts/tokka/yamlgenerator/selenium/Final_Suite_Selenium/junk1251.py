import glob
import os
from datetime import datetime
import json

files = [x for x in os.listdir("C:\\Users\\SC057441\\Desktop\\Any\\pythonscripts\\tokka\\yamlgenerator\\selenium\\Final_Suite_Selenium") if x.startswith("Sce")]
print(files)
date_created = os.path.getmtime("C:\\Users\\SC057441\\Desktop\\Any\\pythonscripts\\tokka\\yamlgenerator\\selenium\\Final_Suite_Selenium" +"\\"+ files[0])
print(date_created)
today_date = datetime.fromtimestamp(date_created).strftime('%Y-%m-%d')
print(today_date)
now = datetime.now()
now = now.strftime("%Y-%m-%d")
if now == today_date:
    print(files[0])