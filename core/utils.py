__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from contextlib import contextmanager, redirect_stdout
from wsgiref.simple_server import make_server
import webbrowser
from io import StringIO

from .constants import UTF8_ENCODAGE


def normalize(content):
    if isinstance(content, str):
        return normalize(content.split('\n'))
    return [str(line).encode(UTF8_ENCODAGE) for line in content]


@contextmanager
def tag(name: str, stream: StringIO, **style):
    with redirect_stdout(stream):
        print("<%s %s>" % (name, ' '.join("%s='%s'" % (k, v) for k, v in style.items())), end='')
        yield
        print("</%s>" % name, end='')


def create_server(addr: str="localhost", port: int=5500, rooter: object=None):
    if rooter:
        print("Starting on {}:{}".format(addr, port))
        serv_http = make_server(addr, port, rooter)
        webbrowser.open("http://{}:{}".format(addr, port))
        return serv_http
    raise ValueError("Le rooter doit être défini !")