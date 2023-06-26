import yaml
import json
from dal import configConverter



read_file_from_config = configConverter.read_config()
write_data_json = configConverter.write_to_json(read_file_from_config)
print(read_file_from_config)





