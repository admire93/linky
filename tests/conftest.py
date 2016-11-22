try:
    from urllib.parse import urlunparse
except ImportError:
    from urlparse import urlunparse

from pytest import fixture


TLD = (
    'com',
    'co.kr',
    'jp',
    'kr',
    'org',
)


def build(protocol, tld, port, host, path, query, fragment):
    netloc = '{}.{}'.format(host, tld)
    if port:
        netloc += ':{}'.format(port)
    actual_url = urlunparse((protocol, netloc, path, '', query, fragment))
    if not protocol:
        actual_url = actual_url[2:]
    return actual_url


@fixture(params=[
    build(protocol, tld, port, host, path, query, fragment)
    for fragment in ('', 'frag')
    for query in ('', 'hello=world', 'hello=world&foo=bar', 'a[0]=a>2')
    for path in ('/', '', '/hello/', 'world.html')
    for tld  in TLD
    for port in ('1234', None)
    for host in ('linky', 'one.linky', 'one.two.linky', '192.168.0.1')
    for protocol in ('https', 'http', '')
])
def fx_url(request):
    return request.param
