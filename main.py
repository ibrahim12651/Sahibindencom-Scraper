from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options


ilan = input("Aranacak İlan linkini giriniz: ")

driver_path = "chromedriver.exe"
service = Service(executable_path=driver_path)

chrome_options = Options()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(service=service, options=chrome_options)


url = ilan
driver.get(url)

time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')

listing = soup.find_all("tr", class_="searchResultsItem")

if listing:
    for item in listing:
        titletag = item.find("a", class_="classifiedTitle")
        title = titletag.text.strip() if titletag else "Başlık Bulunamadı"

        price_tag = item.find("div", class_="classified-price-container")
        price = price_tag.text.strip() if price_tag else "Fiyat Bulunamadı"

        locale_tag = item.find("td", class_="searchResultsLocationValue")
        if locale_tag:
            locale = " ".join([s.strip() for s in locale_tag.stripped_strings])
        else:
            locale = "Konum Bulunamadı"

        print(f"Başlık: {title}")
        print(f"Fiyat: {price}")
        print(f"Konum: {locale}")
        print('--------------------------')

driver.quit()
