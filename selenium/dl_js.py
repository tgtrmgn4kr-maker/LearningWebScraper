from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib import parse
import time
import re



driver = webdriver.Chrome()

url = f"https://swf.com.tw/download/dl_js.html"

driver.implicitly_wait(10)

driver.get(url)

file_set = set()
pattern = re.compile(r'[\w]+\.r(?:ar|\d{2})$')

links = driver.find_elements(By.XPATH, '//a')

for  i in links:
    href = i.get_attribute("href")
    print(href)
    rar = pattern.search(href)
    print(rar)
    if rar:
        file_name = rar.group()
        i.click()
        time.sleep(1)
        file_set.add(file_name)

driver.quit()














