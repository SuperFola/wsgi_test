__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import time

from .constants import *
from .utils import *
from . import forms


def create_header(stream: StringIO) -> str:
    with tag("header", stream):
        with tag("title", stream):
            print("Un zoli site fait main !")
    return stream.getvalue()


def index(env, resp):
    resp(ok, HTML_PAGE)
    s = StringIO()
    s.write(create_header(s))
    with tag("body", s):
        with tag("p", s, bg_color="red", width="50%", center="center"):
            print("Hello world !", end="<br />")
            print("Il est {} !".format(time.strftime("%H:%M:%S")), end="<br />")
            with tag("i", s):
                print("Je suis un beau texte en italic !", end="<br />")
                print("Moi aussi !", end="<br />")
            with tag("b", s):
                print("Sauf que moi j'ai le swag et que je suis en gras héhé ^^", end="<br />")
        with tag("div", s, bg_color="blue", width="75%", align="right"):
            print("Petit Menu !", end="<br />")
            print("Pages disponnibles :", end="<br />")
            with tag("ul", s):
                elems = [
                    "index",
                    "pseudo"
                ]
                for elem in elems:
                    print("<li>%s</li>" % elem)
    return normalize(s.getvalue())


def pseudo(env, resp):
    resp(ok, HTML_PAGE)
    return forms.test_form(env, resp, ('127.0.0.1', 5500))


def info(env, resp):
    resp(ok, HTML_PAGE)
    s = StringIO()
    s.write(create_header(s))
    with tag("body", s):
        with tag("p", s, border="dashed"):
            print("Bonjour ! Ce site a été entièrement créé grâce à une lib fait main !", end="<br />")
            print("Si toi aussi tu veux essayer cette lib, c'est par ici : ", end='')
            with tag("a", s, href="https://github.com/Loodoor/wsgi_test"):
                print("clic moi !", end='<br />')
            print("Tout le code de ce site se trouve dans le fichier main.py du package core :)")
    return normalize(s.getvalue())


def not_found(env, resp):
    resp(page_not_found, HTML_PAGE)
    s = StringIO()
    s.write(create_header(s))
    with tag("body", s):
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