from schema import *

if __name__ == "__main__":
    json_file_converter() # sniffs out json schema in the form of python dictionary

    data_type_converter() # converts python data type to acceptable json format
    
    save_file() # creates new json file for the json schema
