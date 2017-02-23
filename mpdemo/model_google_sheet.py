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

    def get_values(
            self,
            url=None,
            id=None,
            sheet_range=None,
            to_dataframe=False):
        if not any([url, id]):
            raise ValueError('Spreadsheet url or id will be requred.')
#        self.id = url.split('/')[5] if not id else id
        id = url.split('/')[5] if not id else id
        result = self.sheets.values().get(
            spreadsheetId=id, range=sheet_range).execute()
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

    def update(
            self,
            url=None,
            id=None,
            sheet_range=None,
            data=None,
            value_input_option='USER_ENTERED',
            main_dimension='ROWS',
            include_values_in_response='true',
            response_value_render_option='FORMATTED_VALUE',
            response_datetime_render_option='SERIAL_NUMBER'):
        if not any([url, id]):
            raise ValueError('Spreadsheet url or id will be requred.')
        id = url.split('/')[5] if not id else id
        if not all([data.empty, sheet_range]):
            ValueError('data, sheet_range and id ( i.e. spreadsheetId ) will be required.')
        if isinstance(data, pd.DataFrame):
            values = data.values.tolist()
            values.insert(0, data.columns.tolist())
        else:
            values = data
        request_body = {
            'valueInputOption': value_input_option,
            'data': [
                {
                    "range": sheet_range,
                    'majorDimension': main_dimension,
                    'values': values
                }
            ],
            'includeValuesInResponse': include_values_in_response,
            'responseValueRenderOption': response_value_render_option,
            'responseDateTimeRenderOption': response_datetime_render_option
        }
        result = self.sheets.values().batchUpdate(
            spreadsheetId=id, body=request_body).execute()
        if 'error' in result:
            code, message, status = result['error']['code']*1, result['error']['message'], result['error']['status']
        else:
            code = 200
        return code
