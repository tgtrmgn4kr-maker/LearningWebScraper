from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib import parse
from os import path
from pathlib import Path
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")  #Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  #Disable GPU acceleration
chrome_options.add_argument("--window-size=1920,1080")  #Set window size to ensure all elements are visible
chrome_options.add_argument("--ignore-certificate-errors")  #Ignore certificate errors

driver = webdriver.Chrome(options=chrome_options)

search_key = parse.quote("防災包")
url = f"https://www.momoshop.com.tw/search/{search_key}?viewport=desktop&cateLevel=0&_isFuzzy=0&searchType=1"

driver.get(url) #Open the webpage

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//ul[@class='listAreaUl']")
            ))#Wait until the product list is loaded
    shop_items = driver.find_elements(By.XPATH, "//ul[@class='listAreaUl']/li")  #Get all product items

    products_data = []

    print(f"Found {len(shop_items)} items.")

    for i, item in enumerate(shop_items, start=1):  #Iterate through each product item
        product_info = {
            "name" : None,
            "price" : None,
            "link" : None
        }
        item_found = False

        print(f"Item {i}:")

        try:
            name_element = item.find_element(By.XPATH, ".//div[@class='goods-img-url']")  #Get the name element
            product_info["name"] = name_element.get_attribute("title")    

            link_element = item.find_element(By.XPATH, ".//a[@href]")
            product_info["link"] = link_element.get_attribute("href")   #Get the product link

            price_element = item.find_element(By.XPATH, ".//span[@class='price']") #Get the price element
            product_info["price"] = price_element.text.strip()

            item_found = True
            
        except Exception as e:
            print(f"  Error extracting item {i}: {e}")

        if item_found:
            products_data.append(product_info)
            print(f"  Name: {product_info['name']}")
            print(f"  Price: {product_info['price']}")
            print(f"  Link: {product_info['link']}")
        else:
            print("  Item details not found. Skipping.")

    print(f"Total extracted products: {len(products_data)}")

except Exception as e:
    print(f'Specified elements not found: {e}')

finally:
    driver.quit()
    for i in range(len(products_data)):
        print(f'Name: {products_data[i]["name"]} \nPrice: {products_data[i]["price"]} \nLink: {products_data[i]["link"]}\n')
    
    save_path = path.join((Path(__file__).resolve().parent), 'momoshop_products.csv')  # os.path.dirname(path.abspath(__file__)) = pathlib.Path(__file__).resolve().parent
    with open(save_path, 'w', encoding='utf-8') as f:
        r = csv.writer(f)
        r.writerow(['Name', 'Price', 'Link'])
        for product in products_data:
            r.writerow([product['name'], product['price'], product['link']])
            #If you use 'with open', you don't need to close the file explicitly
            

