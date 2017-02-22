from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from logging import getLogger, StreamHandler
from logging import CRITICAL, DEBUG, ERROR, FATAL, INFO, NOTSET, WARNING
import logging

import requests
import sys
pyversion = sys.version_info.major + sys.version_info.minor * 0.1

try:
    from future_builtins import map, filter, zip
except ImportError:
    if pyversion > 2.6 and pyversion < 3:
        raise ImportError(
            'Failed to import future_builtins module.'
            'Contact your computer\'s administrator.')

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs


class Tracker(object):

    def __init__(
            self,
            tracking_id=None,
            output=False,
            log_level='NOTSET',
            output_handler=StreamHandler):
        self.tracking_id = tracking_id
        self.version = 1
        self.aip = 1
        self.endpoint = 'https://www.google-analytics.com/collect'
        self.message = {
            'success':
                '%d : Succeeded to send Measurement Protocol as follows:',
            'failure':
                '%d : Failed to send Measurement Protocol.'
                'See following requests:'
        }
        self.output = output,
        self.log_level = log_level
        level = getattr(logging, self.log_level)
        if level > 0:
            logging.basicConfig(level=level)
            self.logger = getLogger(__name__)
            handler = output_handler()
            handler.setLevel(level)
            self.logger.setLevel(level)

    def show_message(self, message, data):
        print(message)
        print(data)

    def send_request(self, data=None, headers=None):
        response = requests.post(
            self.endpoint,
            data=data,
            headers=headers,
            timeout=5.0)
        status = response.status_code
        if status in range(200, 300):
            message = self.message['success'] % status
        else:
            message = self.message['failure'] % status
        if self.output:
            self.show_message(message, data)
        return status

    def get_payload(self, client_id=None, hit_type=None, data=None):
        if hit_type not in ['pageview', 'event']:
            raise ValueError(
                'hit_type must be pageview or event.')
        if not client_id and not 'cid' in data:
            raise ValueError(
                'Required parameter client_id isn\'t set.')
        payload = {
            'v': self.version,
            'tid': self.tracking_id,
            'aip': self.aip,
            'cid': client_id,
            't': hit_type
        }
        if data:
            payload.update(data)
        return payload

    def send_pageview(
            self,
            client_id=None,
            page=None,
            title=None,
            params=None):
        data = dict()
        if not all([client_id, page]):
            if not all([v in params for v in ['cid', 'dp']]):
                raise ValueError(
                    'Both client_id and page are required.')
        else:
            if not title:
                title = ' '.join(page.split('/')[1:])
            data.update({'dp': page, 'dt': title})
        if params:
            data.update(params)
        data = self.get_payload(client_id, 'pageview', data)
        return self.send_request(data)

    def send_event(
            self,
            client_id=None,
            category=None,
            action=None,
            label=None,
            value=None,
            non_interaction=False,
            params=None):
        data = dict()
        if not all([client_id, category, action]):
            if not all([v in params for v in ['cid', 'ec', 'ea']]):
                raise ValueError(
                    'All client_id, category and action are required.')
        else:
            data.update({'ec': category, 'ea': action})
        if label:
            data.update({'el': label})
        if value:
            data.update({'ev': value})
        if non_interaction:
            data.update({'ni': 1})
        if params:
            data.update(params)
        data = self.get_payload(client_id, 'event', data)
        return self.send_request(data)
