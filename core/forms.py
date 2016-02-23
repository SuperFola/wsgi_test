__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import cgi
import html

from .constants import *
from .utils import normalize


def form_builder(text_field, text_field_name, redirect_to, method, formulaire):
    if text_field_name in formulaire:
        return normalize(html.escape(formulaire.getvalue(text_field_name, "")))
    else:
        return normalize(text_field + '<form method="' + method + '" action="/' + redirect_to + '"><input name="' + text_field_name + '"/></form>')


def test_form(env, resp, addr):
    formulaire = cgi.FieldStorage(fp=env['wsgi.input'], environ=env)

    return form_builder("un pseudo", "pseudo", ':'.join(str(i) for i in addr) + "/pseudo", "get", formulaire)