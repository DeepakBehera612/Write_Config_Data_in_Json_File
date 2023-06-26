import json
import yaml

class configConverter:

    def read_config():

        with open('config.yml','r')as f:
            data = yaml.safe_load(f)
            return data

    
    def write_to_json(data):
        json_object = json.dumps(data)
        with open('output.json', "w") as f:
           
            f.writelines(json_object)
        return json_object
