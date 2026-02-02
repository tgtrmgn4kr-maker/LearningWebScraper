import requests
from tqdm import tqdm
from lxml import html

def download(url):
    file_name = url.split('/')[-1]
    
    response = requests.get(url, headers=header, stream=True)
    with open(file_name, 'wb') as f:
        for data in tqdm(response.iter_content(1024)):
            f.write(data)

    return file_name


url = 'https://swf.com.tw/download/'

header =  {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
           'accept-language' : 'zh-TW,zh;q=0.8,en-US,en;q=0.6'
}

page = requests.get(url, headers=header)

dom = html.fromstring(page.text) 

links = dom.xpath('//a/@href')

for item in links:
    if 'linebot' not in item:
        links.remove(item)
        break

    if 'html' not in item:
        item = url + item

    # Send HEAD request
    head = requests.head(item, headers=header)
    # Get source content type
    MIME = head.headers.get('content-type')

    '''
    Browser determine the attribute of an element rely on their MIME type

    Six elements:
    'linebot.rar', 
    'linebot.r00', 
    'linebot.r01', 
    'linebot.r02', 
    'linebot.r03', 
    '/'
    
    MIMEs
    application/x-rar-compressed
    None    (No content-type)
    None
    None
    None
    text/html
    '''

    if (head.status_code == 200) and (MIME is not 'text/html'):
        print('Downloading url: ',item)
        filename = download(item)
        print(item,'downloaded successfully')








