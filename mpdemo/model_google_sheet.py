from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import pandas as pd


class SpreadSheet(object):
    def __init__(self, service=None):
        if not service:
            raise ValueError('arg service will be required.')
        self.service = service
        self.sheets = self.service.spreadsheets()

    def get_values(self, url=None, id=None, sheet_range=None, to_dataframe=False):
        if not any([url, id]):
            raise ValueError('Spreadsheet url or id will be requred.')
        self.id = url.split('/')[5] if not id else id
        result = self.sheets.values().get(spreadsheetId=self.id, range=sheet_range).execute()
        values = result.get('values', [])
        if to_dataframe:
            headers, values = values[0], values[1:]
            values = pd.DataFrame(values, columns=headers)
        return values
    
    def to_dataframe(self, values=None, headers=None):
        df = pd.DataFrame(values, columns=headers)
        return df
        
    def columns_to_datetime(dataframe=None, columns=None):
        if isinstance(columns, list):
            for c in columns:
                dataframe[c] = pd.to_datetime(dataframe[c])
        elif isinstance(columns, str):
            dataframe[columns] = pd.to_datetime(dataframe[columns])
        else:
            raise ValueError('arg columns must be instance of str or list.')
        return dataframe

