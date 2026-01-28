import gspread
import os
import sys


try:
    creds = os.environ['GOOGLE_CREDENTIALS']
    client = gspread.service_account(creds)
    spreadsheet = client.open('API練習')
    wks = spreadsheet.sheet1

    wks.update_acell('A1', '水果')

    headers = ['名稱', '價格', '數量']

    wks.insert_row(headers)
except Exception as e:
    sys.exit(1)








