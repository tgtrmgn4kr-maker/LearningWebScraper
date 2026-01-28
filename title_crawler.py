from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://vedal.ai/'
driver.get(url)
h1 = driver.find_element(By.XPATH, '//h1')

print('The title "',h1.text,'"')
driver.quit()