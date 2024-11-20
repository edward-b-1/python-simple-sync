
import json

def save_json_config(path:str, config:dict) -> None:
    with open(path, 'w') as ofile:
        ofile.write(json.dumps(config, indent=4))

def load_json_config(path: str) -> dict:
    with open(path, 'r') as ifile:
        config = json.loads(ifile.read())
        return config

