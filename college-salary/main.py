from selenium.webdriver import Chrome
import pandas as pd

CHROME_WEBDRIVER_PATH = "C:/Development/chromedriver.exe"
WEBSITE_URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

driver = Chrome(CHROME_WEBDRIVER_PATH)
driver.maximize_window()
driver.get(WEBSITE_URL)
rows = driver.find_elements_by_css_selector("tr.data-table__row")
ranks = []
majors = []
degrees = []
early_salaries = []
mid_salaries = []
meanings = []

for row in rows:
    early_career, mid_career, meaning = row.find_elements_by_class_name("csr-col--right")
    ranks.append(row.find_element_by_class_name("csr-col--rank").text)
    majors.append(row.find_element_by_class_name("csr-col--school-name").text)
    degrees.append(row.find_element_by_class_name("csr-col--school-type").text)
    early_salaries.append(early_career.text)
    mid_salaries.append(early_career.text)
    meanings.append(meaning.text)

driver.quit()

data = {
    "Rank": ranks,
    "Major": majors,
    "Degree Type": degrees,
    "Early Career Pay": early_salaries,
    "Mid-Career Pay": mid_salaries,
    "Meaning": meanings
}

df = pd.DataFrame(data=data)
print(df.head())
