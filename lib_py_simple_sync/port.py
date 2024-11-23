

from lib_py_simple_sync.constants import default_port

def get_port(config: dict) -> int:
    if 'port' in config:
        return config['port']
    return default_port

