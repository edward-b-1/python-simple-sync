# TODO: should maybe be allowed to monitor files as well as dirs?
# TODO: change `monitor_target` -> `monitor_target`


import socket
import ssl
#import base64
import hashlib

from cryptography.fernet import Fernet

import lib
from lib import calculate_file_hash
from lib.constants import DEFAULT_PORT
from lib.constants import DEFAULT_CONTROL_PORT
from lib.client_config import load_client_config
from lib.client_config import save_client_config
from lib.client_config import create_default_client_config
from lib.client_config import get_monitor_targets
from lib.filesystem import get_linux_config_dir



from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session
from sqlalchemy.orm import Session

def get_changed_monitor_targets(config:dict, session:Session) -> list[...]:

    changed_monitor_targets = []

    for monitor_target in config.get_monitor_targets():
        target_directory = monitor_target['target_directory']
        directory_list = get_directory_list(target_directory)

        for item in directory_list:
            session.query(MonitorTarget).where(MonitorTarget.)


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
    #client_config = lib.client_config._load_client_config_impl('client_config_example.json')
    #print(client_config)
    #print(type(client_config))
    #lib.client_config._save_client_config_impl('client_config_example.out.json', client_config)

    #config_dir = get_linux_config_dir()
    #print(f'{config_dir=}')

    config = None
    try:
        config = load_client_config()
    except:
        create_default_client_config()
        config = load_client_config()

    print(config)

    # create sqlite3 database
    engine = create_engine("sqlite://", echo=True)
    lib.client_db.create_database(engine)

    # for now, store configuration for "watched" directories in the same config
    for monitor_target in get_monitor_targets(config):
        print(f'monitoring path:')
        print(monitor_target)
        # TODO: check it is a directory

        target_directory = monitor_target
        directory_list = get_directory_list(target_directory)
        print(directory_list)

    # need to parse cli TODO
    # for now, just config manually
    # 1. run program for first time, this creates the default config
    # 2. add configuration for monitoring directory

    # listen for messages from push control client and server

    while True:

        # timeout 10ms
        check_messages()

        if message is a push message

            # list of changed targets with md5 and sha256
            changed_monitor_targets = get_changed_monitor_targets()

            send_changed_targets()

            # wait for confirmation
            update_db()

        send_ping()


    return


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM | socket.SOCK_NONBLOCK, 0) as control_socket:
        control_socket.bind(('localhost', DEFAULT_CONTROL_PORT))
        control_socket.listen(10)

        connection, address = control_socket.accept()
        print(f'{connection}, {address}')
        connection.read()
        connection.close()


    with socket.create_connection((hostname, DEFAULT_PORT)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=hostname) as ssocket:
            print(ssocket.version())


if __name__ == '__main__':
    main()
