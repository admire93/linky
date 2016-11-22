# -*- coding: utf-8 -*-
from linky.sub import linky, url_schema


def fullmatch(pattern, s):
    m = pattern.match(s)
    return m and m.group() == s


def test_url_scheme_more():
    # test case in https://mathiasbynens.be/demo/url-regex
    correct = [
        u'http://foo.com/blah_blah',
        u'http://foo.com/blah_blah/',
        u'http://foo.com/blah_blah_(wikipedia)',
        u'http://foo.com/blah_blah_(wikipedia)_(again)',
        u'http://www.example.com/wpstyle/?p=364',
        u'https://www.example.com/foo/?bar=baz&inga=42&quux',
        u'http://✪df.ws/123',
        u'http://142.42.1.1/',
        u'http://142.42.1.1:8080/',
        u'http://➡.ws/䨹',
        u'http://⌘.ws',
        u'http://⌘.ws/',
        u'http://foo.com/blah_(wikipedia)#cite-1',
        u'http://foo.com/blah_(wikipedia)_blah#cite-1',
        u'http://foo.com/unicode_(✪)_in_parens',
        u'http://foo.com/(something)?after=parens',
        u'http://☺.damowmow.com/',
        u'http://code.google.com/events/#&product=browser',
        u'http://j.mp',
        u'http://foo.bar/?q=test%20url-encoded%20stuff',
        u'http://مثال.إختبار',
        u'http://例子.测试',
        u'http://उदाहरण.परीक्षा',
        u'http://a.b-c.de',
    ]
    for c in correct:
        assert fullmatch(url_schema, c), c
    wrong = [
        'http://',
        'http://.',
        'http://..',
        'http://../',
        'http://?',
        'http://??',
        'http://??/',
        'http://#',
        'http://##',
        'http://##/',
        'http://foo.bar?q=Spaces should be encoded',
        '//',
        '//a',
        '///a',
        '///',
        'http:///a',
        'rdar://1234',
        'h://test',
        'http:// shouldfail.com',
        ':// should fail',
        'http://foo.bar/foo(bar)baz quux',
        'ftps://foo.bar/',
        'http://3628126748',
        'http://.www.foo.bar/',
        'http://.www.foo.bar./',
    ]
    for w in wrong:
        assert not fullmatch(url_schema, w), w


def test_url_scheme(fx_url):
    assert fullmatch(url_schema, fx_url), fx_url


def test_linky_escape():
    assert linky('hello<>', escape=True) == 'hello&lt;&gt;'
    assert linky('hello<>', escape=False) == 'hello<>'


def test_linky_substitude(fx_url):
    assert linky('hello {}'.format(fx_url)) == \
        'hello <a href="{0}">{0}</a>'.format(fx_url)
    assert linky('hello {} world'.format(fx_url)) == \
        'hello <a href="{0}">{0}</a> world'.format(fx_url)
    assert linky('hello {0} world {0}'.format(fx_url)) == \
        'hello <a href="{0}">{0}</a> world ' \
        '<a href="{0}">{0}</a>'.format(fx_url)
    assert linky('hello {0} world google.com'.format(fx_url)) == \
        'hello <a href="{0}">{0}</a> world ' \
        '<a href="google.com">google.com</a>'.format(fx_url)
    if fx_url.startswith('http') or fx_url.startswith('https'):
        assert linky(u'hello{} world'.format(fx_url)) == \
            u'hello<a href="{0}">{0}</a> world'.format(fx_url)
