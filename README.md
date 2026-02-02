LearningWebScraper
===
This repository is for recording my learning progress

- `sample.html`: To understand the structure of a html file

## selenium
This directory is for learning how to get information from a webpage by selenium 

### What I practiced
- Using `webdriver.Chrome()` to open a browser
- Using `get()` to get into a specific website
- Using `WebDriverWait` to wait for the appearance of the specific element 
- Using `find_elements(By.XXX,"YYY")` to find elements  

### Notes
- Using `with open()` to make sure that the file being written or read is safe
- Using Chrome with *headless* mode is faster
- It is often better to find a element with its ID because it's unique

### Files
- `selenium_yahoo.py`: To understand the basic operations of selenium
- `selenium_yahoo_2.py`: To get information from a shopping website and then write them down on `momoshop_products.txt`
- `selenium_headless.py` To run Chrome in the **Headless** mode 
- `read_text.py` To get information from `momoshop_products.txt`
- `momoshop_products.txt` To record the information I get from the shopping website

## csv
This directory is for learning the operations of csv

### What I practiced
- Using `csv.read()` to read csv file
- Using `csv.writer().writerow()` to write a row down on csv file 
- Using `zip()` to zip 2 lists

### Notes
- There are two types to read a csv file: `reader()` and `DictReader()`

### Files
- `csv_operate.py`: To use API and write something updating on a Google Sheets file
- `csv_read.py`: To understand the operations of reading csv files
- `csv_write.py`: To write something in `sample.csv`
- `csv_selenium_momo.py`: To get information from a shopping website and then store them in `momoshop_products.csv` and a Google Sheet file
- `momoshop_products.csv`: To store the information from a shopping website
- `sample.csv`: To store test information
- `sheet.py`: To store a method to write something in a Google Sheet file
- `test.py`: To test if `sheet.py` really works         





