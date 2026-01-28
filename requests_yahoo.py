import requests

url = "https://tw.search.yahoo.com/search"
params = {
    "p": "python"
}

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

r = requests.get(url, params=params, headers=headers)

print(r.url)
print(r.status_code)
print(r.text[:500])
