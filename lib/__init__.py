
import base64

required_key_length_characters = 43 # int(math.ceil(256 / 6.0))


def get_fernet_key_from_password(password: str) -> bytes:

    key = password
    base64_key = base64.b64encode(key.encode('utf-8'))

    if len(base64_key) > required_key_length_characters:
        print(f'truncating base64 key from length {len(base64_key)} to length {required_key_length_characters}')
        base64_key = base64_key[:required_key_length_characters]
        base64_key = base64_key + b'='
    elif len(base64_key) < required_key_length_characters:
        raise RuntimeError(f'password input {password} too short')

    return base64_key