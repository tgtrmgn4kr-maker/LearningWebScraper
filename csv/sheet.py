import gspread
import os
import sys

class GoogleSheet:
    def __init__(self, file_name, wks_title=None):
        try:
            creds = os.environ['GOOGLE_CREDENTIALS']
            client = gspread.service_account(creds)
        except:
            print("Google Sheets authentication failed.")
            os._exit(1)

        try:
            sh = client.open(file_name)
        except:
            print(f"Failed to open the spreadsheet: {file_name}")
            os.exit(1)

        if not wks_title:
            self._wks = sh.sheet1
        else:
            try:
                self._wks = sh.worksheet(wks_title)
            except:
                print(f"Failed to open the worksheet: {wks_title}")
                sys.exit(1)
        
    @property
    def headers(self):
        return self._wks.row_values(1)
    
    def update_header(self, data, delete=True):
        if delete:
            pass

        self._wks.insert_row(data, 1)
    
    def append_row(self, data):
        self._wks.append_row(data)
    
    def resize(self, n=1):
        self._wks.resize(n)


    













