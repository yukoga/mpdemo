from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from mpdemo.util import get_credentials, get_service
from mpdemo.tracker import Tracker
from mpdemo.model_google_sheet import SpreadSheet

TRACKING_ID = 'UA-XXXXXX-YY'  # please change to your tracking id.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SHEET_URL = '<YOUR_SPREADSHEET_URL_HERE>'
RANGE = '<YOUR_SHEET_RANGE_HERE>'
KEY_FILE = '<YOUR_KEY_FILE_PATH_HERE>'

discoveryUrl = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
credential = get_credentials(KEY_FILE, scopes=SCOPES)
service = get_service(
    credential,
    discoveryUrl=discoveryUrl,
    service_name='sheets',
    version='v4')

sheet1 = SpreadSheet(service)

df = sheet1.get_values(url=SHEET_URL, sheet_range=RANGE, to_dataframe=True)
params = df[0:1].values[0]
df = df.shift(-1)[:-1]
fields = df.columns.values
param_dict = dict({})
for p, f in zip(params, fields):
    if ',' in p:
        for k in p.split(','):
            param_dict.update({k: f})
    else:
        param_dict.update({p: f})

tracker = Tracker(tracking_id=TRACKING_ID, output=True)
for i, row in df.iterrows():
    params = {k: row[param_dict[k]] for k in param_dict}
    tracker.send_event(params=params)
