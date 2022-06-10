from selenium import webdriver

WEBSITE_URL = "https://www.python.org/"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(WEBSITE_URL)

events = driver.find_elements_by_css_selector("div.event-widget li")

events_dict = {}
for i in range(len(events)):
    events_dict[i] = {
        "time": events[i].find_element_by_tag_name("time").text,
        "name": events[i].find_element_by_tag_name("a").text,
    }

print(events_dict)

driver.quit()   # quit entire program