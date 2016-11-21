""":mod:`linky.sub` --- Substitude URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import re

from markupsafe import escape as html_escape

from .tld import TLD

__all__ = 'linky', 'url_schema'
URL_REGEXP = r'(?P<protocol>https?\:\/\/)?' \
    r'(?P<www>www)?' \
    r'(?P<host>[\w\.\-\_\d]+\.({})(:[\d]+)?\/?)' \
    r'(?P<path>\/[\w\d\/\.]*)?' \
    r'(\?[\w%\d=&]+)?(#[\w\-]*)?'.format('|'.join(TLD))
url_schema = re.compile(URL_REGEXP)


def linky(text, escape=True, **attributes):
    if escape:
        text = html_escape(text)
    return text
