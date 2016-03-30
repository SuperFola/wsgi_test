__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import time

from .constants import *
from .utils import *
from . import forms


def index(env, resp):
    resp(ok, HTML_PAGE)
    s = StringIO()
    with tag("p", s):
        print("Hello world !", end="<br />")
        print("Il est {} !".format(time.time()))
    return normalize(s.getvalue())


def pseudo(env, resp):
    resp(ok, HTML_PAGE)
    return forms.test_form(env, resp, ('127.0.0.1', 5500))


def not_found(env, resp):
    resp(page_not_found, HTML_PAGE)
    s = StringIO()
    with tag("center", s):
        with tag("h1", s, style="color: red;"):
            print("Erreur 404")
        print("La page n'a pas pu être trouvée ...")
    return normalize(s.getvalue())


def rooter(env, resp):
    pages = {
        '/': index,
        '/pseudo': pseudo
    }

    for addr, view in pages.items():
        if env['PATH_INFO'] == addr:
            return view(env, resp)

    return not_found(env, resp)