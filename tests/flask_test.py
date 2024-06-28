import socket
from controllers.controller import get_port_from_config


def test_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = get_port_from_config()
    s.connect(('localhost',port))
