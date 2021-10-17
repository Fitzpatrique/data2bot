'''
Write a genertic program that:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)
'''

# import the necessary libraries

import json
from json.decoder import JSONDecodeError
import time
import os

file2 = input("Enter the json file path: ") # takes in the json file path as an input string
schema = {} # instantiate an empty dictionary object

try:
    with open(file2, mode = 'r+', encoding = 'utf-8') as f:
        try:
            data = json.load(f) # load json file as a python dictionary

            def json_file_converter(): # sniffs out json schema in the form of python dictionary
                global data
                for i in data["message"].items():
                    schema[i[0]] = {
                        "type": type(i[1]),
                        "tag": "",
                        "description": "",
                        "required": False}
                return schema

            def data_type_converter(): # converts python data type to acceptable json format
                global schema
                for i in list(schema.keys()):
                    if schema[i]["type"] == int:
                        schema[i]["type"] = 'integer'
                    elif schema[i]["type"] == str:
                        schema[i]["type"] = 'string'
                    elif schema[i]["type"] == list or schema[i]["type"] == tuple:
                        schema[i]["type"] = 'enum'
                    elif schema[i]["type"] == dict:
                        schema[i]["type"] = 'array'
                    elif schema[i]["type"] == bool and data["message"][i] == True:
                        schema[i]["type"] = True
                    elif schema[i]["type"] == bool and data["message"][i] == False:
                        schema[i]["type"] = False

                return schema

            def save_file(): # creates new json file for the json schema
                global schema
                path = "schema"

                # check if directory to store json schema exists

                if os.path.isdir(path) == False: # create new directory if it doesn't exist
                    os.mkdir(path)
       
                if schema == {}:
                    pass

                elif len(schema) > 1:
                    with open(path + "\schema_2.json", "w+") as outfile:
                        json.dump(schema, outfile)
                        print(f"File saved successfully in {path}\schema_2.json")
                        time.sleep(10)

        except JSONDecodeError: # catch error that occurs when the json file is empty
            print("JSON file is empty")
            time.sleep(10)
            quit()

except FileNotFoundError: # catch error that occurs when the file / file path is not found
    print(f"No such file or directory: {file2}")
    time.sleep(10)
    quit()
    