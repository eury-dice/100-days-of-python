from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import requests
import re

FORM_URL = "https://forms.gle/jb5ww4BL5Wsd7N2H7"
BASE_RENTAL_URL = "https://www.zillow.com"
RENTAL_LISTING_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.6471850210328%2C%22north%22%3A37.90317628965597%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(url=RENTAL_LISTING_URL, headers=HEADERS)

soup = BeautifulSoup(response.text, "lxml")
rentals = soup.select("div.list-card-info")
addresses = []
prices = []
links = []

for rental in rentals:
    # for addresses
    addresses.append(rental.a.address.text)
    # for prices
    price = re.split('\+|/| ', rental.div.next_sibling.div.text)[0]
    prices.append(price)
    # for links
    link = rental.a['href']
    if BASE_RENTAL_URL in link:
        links.append(link)
    else:
        links.append((BASE_RENTAL_URL + link))

# Adding data to Form
driver = Chrome(CHROME_DRIVER_PATH)
driver.get(FORM_URL)
driver.maximize_window()

for i in range(len(addresses)):
    inputs = driver.find_elements_by_css_selector("input.quantumWizTextinputPaperinputInput.exportInput")

    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])

    submit = driver.find_element_by_css_selector("div.appsMaterialWizButtonEl")
    submit.click()

    next_query = driver.find_element_by_tag_name("a")
    next_query.click()

driver.quit()
