# mpdemo
## What's this ?
This is an experimental library to deal with Google Analytics Measurement
Protocol and Google Spreadsheet.  
Once you've installed this library into your python environment, you can get
data from Google Spreadsheet and send those data to Google Analytics with
Measurement Protocol.  

## Prerequisites  
- Python 3+ (Would work with Python 2.7+, but it's not been tested.)  
- Google Spreadsheet
- Google API's service account secret json.   
  - You will be required to create "service account" which enable you to access
Google APIs. For this library, you also need to have service account keyfile
in JSON format.  
Please take a look at following document to get service account keyfile.  
    - [Google Identity
      Platform](https://developers.google.com/identity/protocols/OAuth2ServiceAccount)  
    - [Google Sheets API - Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)

## How to install
pip install git+https://github.com/yukoga/mpdemo.git  

## Tracker object usage  
mpdemo module support for sending pageview and event hit by send_pageview()
and send_event() method. Here is sample implementations. 
```python
# Instantiate tracker object.  
tracker = Tracker(tracking_id='UA-XXXXXXX-YY', output=True)

# send pageview.
params = {
  'client_id': '1234567.8901234',
  'page': '/some/page/path.html'
}
tracker.send_pageview(params);

# send event
params = {
  'client_id': '1234567.8901234',
  'category': 'offline tracking',
  'action': 'offline purchase',
  'label': 'some_product_name',
  'value': 10000
}
tracker.send_event(params)
```

## Sample script usage  
The sample script ( example/send_mp_from_spreadsheet.py ) is used for
demonstration which send Measurement Protocol based on data stored in Google
Spreadsheet.  

To use sample script ( example/send_mp_from_spreadsheet.py ), you need to
follow below steps.  

1. Get service account credentials in JSON format from [Google API
   service account page](https://console.developers.google.com/permissions/serviceaccounts).  
   For more details, take a look developer guide for [Google Identity
   Platform](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount)
2. Download sample script from https://raw.githubusercontent.com/yukoga/mpdemo/master/example/send_mp_from_spreadsheet.py and locate it into a directory where service account keyfile exists. 
3. Set your own value into the following parameters in the sample script.  
    - TRACKING_ID : Google Analytics property ID.  
    - SHEET_URL : Google Spreadsheet URL.  
    - RANGE : Spreadsheet range which contains data to be sent to
      Google Analytics by Measurement Protocol.  
    - KEY_FILE : service account keyfile path.
4. Execute sample script as follows:  
    - python send_mp_from_spreadsheet.py

### Spreadsheet format  
This sample script can send any data on Spreadsheet specified by RANGE
parameter, but it should have following format as required.  
- Column A is assigned for last update timestamp which is populated by
  send_mp_from_spreadsheet.py.   
- The row just above data should contains Measurement Protocol parameter name
  like cid, dp ... etc.  

Take a look at [this example spreadsheet](https://docs.google.com/spreadsheets/d/1lxBu7Zhl8X1ImqvrNFxhYGDGHGYJkY2nDSYBZioJ5XU/edit#gid=284780649).
