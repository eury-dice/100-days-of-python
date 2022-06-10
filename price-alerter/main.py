from bs4 import BeautifulSoup
import requests
import smtplib
import os

ITEM_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-US,en;q=0.5",
}
HOST = os.environ["HOST"]
PORT = os.environ["PORT"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDER_PASS = os.environ["SENDER_PASS"]
MIN_PRICE = float(os.environ["MIN_PRICE"])

response = requests.get(url=ITEM_URL, headers=HEADERS)

soup = BeautifulSoup(response.text, "lxml")
price_text = soup.find(name="span", id="priceblock_ourprice").getText()
price = float(price_text.strip("$"))

if price <= MIN_PRICE:
    product = soup.find(name="h1", id="title").getText().strip()
    message = f"{product} is now only {price_text}\n{ITEM_URL}"

    with smtplib.SMTP(HOST, PORT) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASS)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=RECEIVER_EMAIL,
                            msg=f"From: {SENDER_EMAIL}\n"
                                f"To: {RECEIVER_EMAIL} \n"
                                f"Subject:Amazon Price Alert\n\n"
                                f"{message}".encode("utf-8"))
