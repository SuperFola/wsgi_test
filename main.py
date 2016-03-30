__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import core


if __name__ == '__main__':
    serv_http = core.utils.create_server(rooter=core.main.rooter)
    serv_http.serve_forever()