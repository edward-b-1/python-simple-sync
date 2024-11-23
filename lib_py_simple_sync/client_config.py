
#import os
import pathlib

# TODO: use absolute path
from .json_config import save_json_config
from .json_config import load_json_config

from lib_py_simple_sync.filesystem import get_linux_config_dir

DEFAULT_CLIENT_CONFIG_FILENAME = 'client_config.json'

def save_client_config(config:dict) -> None:
    _save_client_config_impl(_get_client_config_default_path(), config)

def load_client_config() -> dict:
    return _load_client_config_impl(_get_client_config_default_path())

def _save_client_config_impl(path:str, config:dict) -> None:
    save_json_config(path, config)

def _load_client_config_impl(path: str) -> dict:
    return load_json_config(path)

def _get_client_config_default_path() -> str:
    config_dir = get_linux_config_dir()
    config_filename = DEFAULT_CLIENT_CONFIG_FILENAME
    return f'{config_dir}/{config_filename}'

def _get_default_client_config() -> dict:
    client_config = {
        'port': 12346,
        'ping_delay_seconds': 1,
        'data_directory': 'not_used',
        'monitor_targets': [],
    }
    return client_config

def create_default_client_config() -> None:
    config_dir = get_linux_config_dir()
    pathlib.Path(config_dir).mkdir(parents=True, exist_ok=True)
    client_config = _get_default_client_config()
    client_config_default_path = _get_client_config_default_path()
    _save_client_config_impl(client_config_default_path, client_config)

def get_monitor_targets(config:dict):
    return config['monitor_targets']

