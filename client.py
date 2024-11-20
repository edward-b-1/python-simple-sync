

import socket
import ssl
#import base64
import hashlib

from cryptography.fernet import Fernet

import lib
from lib import calculate_file_hash
from lib.constants import default_port
from lib.client_config import load_client_config
from lib.client_config import save_client_config
from lib.client_config import create_default_client_config
from lib.filesystem import get_linux_config_dir


def main():

    target_directory = './example-target-directory'
    directory_list = lib.get_directory_list(target_directory)
    print('directory_list:')
    print(directory_list)

    password = "JuliaJuliaJuliaJuliaJuliaJuliaJulia"
    hashed_password = hashlib.sha256(password.encode('utf-8'))
    hash_digest = hashed_password.digest()
    print(f'{hashed_password.hexdigest()}')
    base64_key = lib.get_fernet_key_from_password_2(password)
    print(f'Base64 encoded key is: {base64_key}')

    fernet_instance = Fernet(base64_key)
    token = fernet_instance.encrypt(b"some example content to encrypt")
    print(token)
    print(fernet_instance.decrypt(token))

    hostname = 'localhost'
    context = ssl._create_unverified_context()

    path = 'example-file.txt'
    file_hash = calculate_file_hash(path)
    print(f'{file_hash=}')

    # tests
    #client_config = load_client_config('client_config_example.json')
    #print(client_config)
    #print(type(client_config))
    #save_client_config('client_config_example.out.json', client_config)

    #config_dir = get_linux_config_dir()
    #print(f'{config_dir=}')

    config = None
    try:
        config = load_client_config()
    except:
        create_default_client_config()
        config = load_client_config()

    print(config)

    # for now, store configuration for "watched" directories in the same config


    # need to parse cli TODO
    # for now, just config manually
    # 1. run program for first time, this creates the default config
    # 2. add configuration for monitoring directory


    return

    with socket.create_connection((hostname, default_port)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=hostname) as ssocket:
            print(ssocket.version())


if __name__ == '__main__':
    main()
