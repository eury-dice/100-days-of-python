from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "https://en.wikipedia.org/wiki/Main_Page"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(WEBSITE_URL)

article_count = driver.find_element_by_css_selector("#articlecount a")
all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

driver.get(driver.current_url)
search = driver.find_element_by_id("searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
