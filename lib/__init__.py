
import io
import base64
import hashlib
import os
#import math


#required_key_length_characters = 43 # int(math.ceil(256 / 6.0))


def get_fernet_key_from_password_2(password: str) -> bytes:

    key = password
    hashed_key = hashlib.sha256(key.encode('utf-8'))
    hashed_key_digest = hashed_key.digest()
    base64_key = base64.b64encode(hashed_key_digest)
    #print(f'len: {len(base64_key)}')
    return base64_key

# def get_fernet_key_from_password(password: str) -> bytes:
#     key = password
#     base64_key = base64.b64encode(key.encode('utf-8'))

#     if len(base64_key) > required_key_length_characters:
#         print(f'truncating base64 key from length {len(base64_key)} to length {required_key_length_characters}')
#         base64_key = base64_key[:required_key_length_characters]
#         base64_key = base64_key + b'='
#     elif len(base64_key) < required_key_length_characters:
#         raise RuntimeError(f'password input {password} too short')

#     return base64_key


def get_directory_list(target_directory: str) -> list[(str, str)]:
    path = target_directory

    if os.path.isfile(path):
        return [(path, 'f')]

    elif os.path.isdir(path):
        items = [(path, 'd')]
        # TODO: map
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            more_items = get_directory_list(full_path)
            items.extend(more_items)
        return items

    return []


def calculate_file_hash(file_path: str) -> bytes:
    with open(file_path, "rb") as ifile:
        #digest = hashlib.file_digest(ifile, "sha256")
        #sha256sum = hashlib.file_digest(ifile, 'sha256').hexdigest()
        sha256sum = hashlib.sha256(ifile.read()).hexdigest()
        return sha256sum
    

