import pytest
from mpdemo.tracker import Tracker


@pytest.fixture
def mpsample():
    d = dict()
    d['tracking_id'] = 'UA-123456-78'
    d['log'] = True
    d['pageview'] = {
        'page': '/test/for/Measurement/Protocol/index.html',
        'title': 'This is Measurement Protocol test - 日本語'
    }
    d['event'] = {
        'category': 'Some Event Category',
        'action': 'Some Action',
        'label': 'Some Event Label',
        'value': 1000,
        'non-interaction': False
    }
    d['cd1'] = {
        'page': '/test/for/Measurement/Protocol/index.html',
        'title': 'This is Measurement Protocol test - 日本語',
        'params': {'cd1': 'dimension1 value - カスタム ディメンション１'}
    }
    d['tracker'] = Tracker(d['tracking_id'], log=d['log'])
    return d


def test_send_pageview(mpsample):
    payload = '''{'v': 1, 'tid': 'UA-123456-78',
    'dt': 'This is Measurement Protocol test - 日本語',
    'cid': 12345, 't': 'pageview',
    'dp': '/test/for/Measurement/Protocol/index.html', 'aip': 1}'''
    # assert payload == mpsample['tracker'].send_pageview(
    assert None is mpsample['tracker'].send_pageview(
        12345, page=mpsample['pageview']['page'],
        title=mpsample['pageview']['title'])
