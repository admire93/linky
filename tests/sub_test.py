try:
    from urllib.parse import urlunparse
except ImportError:
    from urlparse import urlunparse

from pytest import mark

from linky.sub import URL_REGEXP, linky, url_schema
from linky.tld import TLD


@mark.parametrize('fragment', ('', 'frag'))
@mark.parametrize('query', ('', 'hello=world', 'hello=world&foo=bar'))
@mark.parametrize('path', ('/', '', '/hello/', 'world.html'))
@mark.parametrize('tld', TLD)
@mark.parametrize('port', ('1234', None))
@mark.parametrize('host', ('linky', 'one.linky', 'one.two.linky'))
@mark.parametrize('protocol', ('https', 'http', ''))
def test_url_scheme(protocol, tld, port, host, path, query, fragment):
    netloc = '{}.{}'.format(host, tld)
    if port:
        netloc += ':{}'.format(port)
    actual_url = urlunparse((protocol, netloc, path, '', query, fragment))
    if not protocol:
        actual_url = actual_url[2:]
    assert url_schema.match(actual_url), URL_REGEXP


def test_linky():
    assert linky('hello<>', escape=True) == 'hello&lt;&gt;'
    assert linky('hello<>', escape=False) == 'hello<>'
    assert linky('hello http://google.com') == \
        'hello <a href="http://google.com">http://google.com</a>'
    assert linky('hello https://google.com') == \
        'hello <a href="https://google.com">http://google.com</a>'
