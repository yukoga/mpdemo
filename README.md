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

## How to install & use sample script   
1. pip install git+https://github.com/yukoga/mpdemo.git  
2. Download sample script from
   https://github.com/yukoga/mpdemo/blob/master/example/send_mp_from_spreadsheet.py
   and locate it into a directory where service account keyfile exists. 
3. Set your own value into the following parameters in the sample script.  
    - tracking id ( TRACKING_ID ) 
    - spreadsheet URL ( SHEET_URL )  
    - sheet range ( RANGE ) 
    - key file ( KEY_FILE ) 
4. Execute sample script as follows:  
    - python send_mp_from_spreadsheet.py
