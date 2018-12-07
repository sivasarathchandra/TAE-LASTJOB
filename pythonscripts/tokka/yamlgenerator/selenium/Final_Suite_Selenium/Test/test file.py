import json
import pprint

data_dict={}

with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//Age_category_Input.json", "r")as readfile:
    data_dict = json.load(readfile)

pprint.pprint(data_dict)