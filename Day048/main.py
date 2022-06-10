from selenium import webdriver

WEBSITE_URL = "http://secure-retreat-92358.herokuapp.com/"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(WEBSITE_URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("John")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Doe")
email = driver.find_element_by_name("email")
email.send_keys("john.doe@mail.com")
button = driver.find_element_by_tag_name("button")
button.click()
