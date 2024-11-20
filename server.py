

import socket
import ssl

from lib.constants import DEFAULT_PORT

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.crt', 'server.key')


def main():

    # TODO: should the server be non-blocking and send its own Server pings?

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
        server_socket.bind(('0.0.0.0', DEFAULT_PORT))
        server_socket.listen(10)
        with context.wrap_socket(server_socket, server_side=True) as ssl_socket:

            while True:
                connection, address = ssl_socket.accept()
                print(f'{connection}, {address}')

                connection.close()


if __name__ == '__main__':
    main()
