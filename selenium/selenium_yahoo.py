from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://tw.yahoo.com")

s_f = driver.find_element(By.NAME,'p')
s_f.send_keys('超圖解Python物聯網')
s_f.submit()
time.sleep(3)
driver.back()
time.sleep(3)

s_f = driver.find_element(By.XPATH,"//input[@name='p']")
s_f.send_keys('超圖解Python物聯網')
s_f = driver.find_element(By.ID,"header-desktop-search-button")
s_f.click()

time.sleep(3)
driver.quit()


