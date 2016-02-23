__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .constants import UTF8_ENCODAGE


def normalize(*content):
    return [str(line).encode(UTF8_ENCODAGE) for line in content]