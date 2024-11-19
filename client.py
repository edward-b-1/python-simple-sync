

import socket
import ssl
#import base64
import hashlib

from cryptography.fernet import Fernet

import lib
from lib.constants import default_port


def main():

    target_directory = './example-target-directory'
    directory_list = lib.get_directory_list(target_directory)
    print(directory_list)

    generated_key = Fernet.generate_key()
    print(f'Example generated key: {generated_key}')
    print(f'Length of example key: {len(generated_key)}')

    password = "JuliaJuliaJuliaJuliaJuliaJuliaJulia"
    hashed_password = hashlib.sha256(password.encode('utf-8'))
    hash_digest = hashed_password.digest()
    print(f'{hashed_password.hexdigest()}')
    #base64_key = lib.get_fernet_key_from_password(password)
    #print(f'Base64 encoded key is: {base64_key}')
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

    return

    with socket.create_connection((hostname, default_port)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=hostname) as ssocket:
            print(ssocket.version())


if __name__ == '__main__':
    main()
