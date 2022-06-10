from selenium import webdriver

WEBSITE_URL = "https://www.python.org/"
# FIREFOX_DRIVER_PATH = "C:/Development/geckodriver.exe"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

# driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(WEBSITE_URL)

# search_bar = driver.find_element_by_name("q")
# print(search_bar)

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# docu_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(docu_link.text)

bug_link = driver.find_element_by_xpath("/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)

# driver.close()  # only one tab
driver.quit()   # quit entire program
