__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import time

from .constants import *
from .utils import normalize
from . import forms


def index(env, resp):
    resp(ok, HTML_PAGE)
    return normalize("Hello world !", time.time())


def pseudo(env, resp):
    resp(ok, HTML_PAGE)
    return forms.test_form(env, resp, ('127.0.0.1', 5500))


def not_found(env, resp):
    resp(page_not_found, HTML_PAGE)
    return normalize("<center><h1 style=\"color: red;\">Erreur 404</h1>", "La page n'a pas pu être trouvée ...</center>")


def rooter(env, resp):
    pages = {
        '/': index,
        '/pseudo': pseudo
    }

    for addr, view in pages.items():
        if env['PATH_INFO'] == addr:
            return view(env, resp)

    return not_found(env, resp)