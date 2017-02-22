from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from mpdemo.util import get_credentials, get_service
from mpdemo.tracker import Tracker
from mpdemo.model_google_sheet import SpreadSheet

TRACKING_ID = 'UA-XXXXXX-YY' # please change to your tracking id. 
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
discoveryUrl = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
credential = get_credentials('service-account.json', scopes=SCOPES)
service = get_service(credential, discoveryUrl=discoveryUrl, service_name='sheets', version='v4')

sheet_url = "https://docs.google.com/spreadsheets/d/1lxBu7Zhl8X1ImqvrNFxhYGDGHGYJkY2nDSYBZioJ5XU/edit#gid=284780649"
rangeName = 'new CRM!A1:J'
sheet1 = SpreadSheet(service)

df = sheet1.get_values(url=sheet_url, sheet_range=rangeName, to_dataframe=True)
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

print(param_dict)

for i, row in df.iterrows():
    params = { k: row[param_dict[k]] for k in param_dict}

    tracker.send_event(params=params)
