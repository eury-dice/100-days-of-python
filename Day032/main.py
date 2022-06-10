import smtplib
import random
import datetime as dt

QUOTES_FILE = "quotes.txt"
GMAIL_HOST = "smtp.gmail.com"
YAHOO_HOST = "smtp.mail.yahoo.com"
PORT = 587
SEND_DAY = 4  # Monday

USER_EMAIL = "jericho.ardent@gmail.com"
# RECIPIENT_EMAIL = "jericho.ardent@yahoo.com"
PASSWORD = "The wall$ must h0ld"

# USER_EMAIL = "jericho.ardent@yahoo.com"
RECIPIENT_EMAIL = "jericho.ardent@gmail.com"
# PASSWORD = "odjpdbenxumofrzx"   # Generated password from Yahoo!

weekday = dt.datetime.now().weekday()

if weekday == SEND_DAY:
    with open(QUOTES_FILE, "r") as file:
        quotes = [line for line in file.readlines()]
    quote = random.choice(quotes)
    with smtplib.SMTP(GMAIL_HOST, PORT) as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=USER_EMAIL,
                            to_addrs=RECIPIENT_EMAIL,
                            msg=f"From: {USER_EMAIL}\n"
                                f"To: {RECIPIENT_EMAIL}\n"
                                f"Subject:Monday Motivation\n\n{quote}")
else:
    print("No quote for today.")
