from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from mpdemo.util import get_credentials, get_service
from mpdemo.tracker import Tracker
from mpdemo.model_google_sheet import SpreadSheet

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
discoveryUrl = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
credential = get_credentials('service-account.json', scopes=SCOPES)
service = get_service(mycreden, discoveryUrl=discoveryUrl, service_name='sheets', version='v4')

sheet_url = "https://docs.google.com/spreadsheets/d/1lxBu7Zhl8X1ImqvrNFxhYGDGHGYJkY2nDSYBZioJ5XU/edit#gid=284780649"
rangeName = 'new CRM!A1:J'

df = sheet1.get_values(id=spreadsheetId, sheet_range=rangeName, to_dataframe=True)
df.head()