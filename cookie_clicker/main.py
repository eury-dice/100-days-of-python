from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from time import time   # , sleep

CHROME_WEBDRIVER_PATH = "C:/Development/chromedriver.exe"
WEBSITE_URL = "https://orteil.dashnet.org/cookieclicker/"
MINUTES = 5
SECONDS_CHECK = 5

driver = Chrome(CHROME_WEBDRIVER_PATH)
driver.maximize_window()
driver.get(WEBSITE_URL)


def check_upgrades():
    upgrades = driver.find_elements_by_css_selector("div.product.unlocked.enabled")
    upgrades = upgrades[::-1]

    for upgrade in upgrades:
        if upgrade.is_enabled():
            driver.execute_script("arguments[0].scrollIntoView();", upgrade)
            upgrade.click()
            break


timeout = time() + (60 * MINUTES)

while timeout > time():
    check_time = time() + SECONDS_CHECK
    while True:
        cookie = driver.find_element_by_id("bigCookie")
        cookie.click()
        if check_time <= time():
            check_upgrades()
            break

# while True:
#     try:
#         cookies = driver.find_element_by_css_selector("#cookies div")
#         print(f"Cookies/sec: {cookies.text.split(' : ')[1]}")
#         break
#     except StaleElementReferenceException:
#         sleep(1)

try:
    cookies = WebDriverWait(driver, 20, ignored_exceptions=StaleElementReferenceException) \
        .until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#cookies div")))
    print(f"Cookies/sec: {cookies.text.split(' : ')[1]}")
finally:
    driver.quit()
