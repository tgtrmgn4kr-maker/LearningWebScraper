import requests
from tqdm import tqdm

def download(url):
    file_name = url.split('/')[-1]
    
    response = requests.get(url, headers=header, stream=True)
    with open(file_name, 'wb') as f:
        for data in tqdm(response.iter_content(1024)):
            f.write(data)

    return file_name

url = '	https://swf.com.tw/images/life/Europe2023/kv_15.jpg'

header = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
           'accept-language' : 'zh-TW,zh;q=0.8,en-US,en;q=0.6'
}

download(url)



