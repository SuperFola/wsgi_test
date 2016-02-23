__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from wsgiref.simple_server import make_server

import core


if __name__ == '__main__':
    addr = 'localhost'
    port = 5500
    print("Starting on {}:{}".format(addr, port))
    serv_http = make_server(addr, port, core.main.rooter)
    serv_http.serve_forever()