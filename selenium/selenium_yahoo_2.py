from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib import parse
from os import path
from pathlib import Path

driver = webdriver.Chrome()
search_key = parse.quote("防災包")

url = f"https://www.momoshop.com.tw/search/{search_key}?viewport=desktop&cateLevel=0&_isFuzzy=0&searchType=1"
driver.get(url) #Open the webpage

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//ul[@class='listAreaUl']")
            ))#Wait until the product list is loaded
    
    shop_items = driver.find_elements(By.XPATH, "//ul[@class='listAreaUl']/li")  #Get all product items

    products_data = [] #List to store product information

    print(f"Found {len(shop_items)} items.")

    for i, item in enumerate(shop_items, start=1):
        product_info = {
            "name" : None,
            "price" : None,
            "link" : None
        }
        item_found = False

        print(f"Item {i}:")

        try:
            link_element = item.find_element(By.XPATH, ".//a[@href]")

            product_info["link"] = link_element.get_attribute("href")
            product_info["name"] = item.find_element(By.XPATH, ".//div[@class='goods-img-url']").get_attribute("title")
            price_element = item.find_element(By.XPATH, ".//span[@class='price']")
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
    save_path = path.join((Path(__file__).resolve().parent), 'momoshop_products.txt')  # os.path.dirname(path.abspath(__file__)) = pathlib.Path(__file__).resolve().parent
    with open(save_path, 'w', encoding='utf-8') as f:
        for product in products_data:
            f.write(f"Name: {product['name']}\n")
            f.write(f"Price: {product['price']}\n")
            f.write(f"Link: {product['link']}\n")
            f.write("\n")
        #If you use 'with open', you don't need to close the file explicitly
