from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import os
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client.file import Storage
from oauth2client.service_account import ServiceAccountCredentials


def get_credentials(
        keyfile_path=None,
        scopes=None,
        credential_file='credentials-googleapis.json'):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, credential_file)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            keyfile_path, scopes=scopes)
    return credentials


def get_service(
        credentials=None,
        discoveryUrl=None,
        service_name=None,
        version=None):
    http = credentials.authorize(httplib2.Http())
    service = discovery.build(
        service_name,
        version,
        http=http,
        discoveryServiceUrl=discoveryUrl)
    return service
