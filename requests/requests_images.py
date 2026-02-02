import requests
from lxml import html
from tqdm import tqdm


def download(url):
    file_name = url.split('/')[-1]
    
    response = requests.get(url, headers=header, stream=True)
    with open(file_name, 'wb') as f:
        for data in tqdm(response.iter_content(1024)):
            f.write(data)

    return file_name

url = 'https://swf.com.tw/scrap/'

header =  {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
           'accept-language' : 'zh-TW,zh;q=0.8,en-US,en;q=0.6'
}

page = requests.get(url, headers=header) # string

# Analyze html source code
dom = html.fromstring(page.text) 

images = dom.xpath('//img/@src') # type: list

for item in images:
    if not item.startswith('http'):
        item = url + item

    # Send HEAD request
    head = requests.head(item, headers=header)
    # Get source content type
    MIME = head.headers.get('content-type')

    # Check if files exist
    if (head.status_code == 200) and ('image' in MIME):
        print('Downloading url: ', item)
        file = download(item)
        print(file, ' download complete!') 



















