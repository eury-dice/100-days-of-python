from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from os import environ
import smtplib

CHROME_WEBDRIVER_PATH = environ["CHROME_WEBDRIVER_PATH"]
WEBSITE_URL = environ["WEBSITE_URL"]
HOST = environ["HOST"]
PORT = environ["PORT"]
SENDER = environ["SENDER_EMAIL"]
PASS = environ["SENDER_PASSWORD"]
RECEIVER = environ["RECEIVER_EMAIL"]


class InternetSpeedBot:
    def __init__(self, up_min, down_min):
        self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
        self.up_min = up_min
        self.down_min = down_min
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get(WEBSITE_URL)
        go_button = self.driver.find_element_by_css_selector("a.js-start-test.test-mode-multi")
        go_button.click()

        try:
            WebDriverWait(self.driver, 180, ignored_exceptions=NoSuchElementException)\
                .until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.result-container-speed-active")))
            self.down = float(self.driver.find_element_by_css_selector("span.download-speed").text)
            self.up = float(self.driver.find_element_by_css_selector("span.upload-speed").text)
        finally:
            print(f"Download: {self.down}, Upload: {self.up}")
            self.driver.quit()
            if self.down < self.down_min or self.up < self.up_min:
                self.send_notification()
            else:
                print("Internet speed is good or better than expected.")

    def send_notification(self):
        message = f"Your current download/upload speed is not up to par!\n" \
                  f"You expected download/upload as {self.down_min}Mbps/{self.up_min}Mbps but it is actually " \
                  f"{self.down}Mbps/{self.up}Mbps.\n\nContact your ISP!"
        with smtplib.SMTP(HOST, PORT) as connection:
            connection.starttls()
            connection.login(SENDER, PASS)
            connection.sendmail(from_addr=SENDER,
                                to_addrs=RECEIVER,
                                msg=f"From: {SENDER}\n"
                                    f"To: {RECEIVER} \n"
                                    f"Subject:Download/Upload is Below Expectations\n\n"
                                    f"{message}")
