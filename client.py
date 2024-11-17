

import socket
import ssl
import base64
import math

from cryptography.fernet import Fernet

from lib.constants import default_port


def main():

    generated_key = Fernet.generate_key()
    print(f'Example generated key: {generated_key}')
    print(f'Length of example key: {len(generated_key)}')

    required_key_length_bits = 256 # 32 * 8
    required_key_length_bytes = required_key_length_bits / 8
    required_key_length_characters = int(math.ceil(required_key_length_bits / 6.0))
    print(f'required_key_length_characters={required_key_length_characters}')

    key = "JuliaJuliaJuliaJuliaJuliaJuliaJulia"
    #key = "1234567890123456789012345678901234567890"
    print(f'Encryption key is: {key}')
    base64_key = base64.b64encode(key.encode('utf-8'))
    print(f'Base64 encoded key is: {base64_key}')
    print(f'Length of base64 encoded key: {len(base64_key)}')
    if len(base64_key) > required_key_length_characters:
        base64_key = base64_key[:required_key_length_characters]
        print(f'Truncating key to length {required_key_length_characters}: {base64_key}')
        print(f'Length of base64 encoded key is now {len(base64_key)}')
        base64_key = base64_key + b'='
        print(f'Adding padding: {base64_key}')
        print(f'Length of base64 encoded key is now {len(base64_key)}')
    elif len(base64_key) < required_key_length_characters:
        print(f'error: key is too short')
        raise RuntimeError(f'key too short')

    fernet_instance = Fernet(base64_key)
    token = fernet_instance.encrypt(b"some example content to encrypt")
    print(token)
    print(fernet_instance.decrypt(token))

    hostname = 'localhost'
    context = ssl._create_unverified_context()

    with socket.create_connection((hostname, default_port)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=hostname) as ssocket:
            print(ssocket.version())


if __name__ == '__main__':
    main()
