import sheet
from datetime import datetime

gs = sheet.GoogleSheet('API練習')

def main():
    print("Current Headers:", gs.headers)

    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    gs.append_row([dt, '蘋果', 50, '123.com'])

if __name__ == '__main__':
    main()









