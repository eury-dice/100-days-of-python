from random import randint
from datetime import datetime
import pandas as pd
import smtplib

HOST = "smtp.gmail.com"
PORT = 587
SENDER_EMAIL = "jericho.ardent@gmail.com"
SENDER_PASS = "The wall$ must h0ld"
BIRTHDAYS_FILE = "./birthdays.csv"
LETTER_X_FILE = "./letter_templates/letter_[X].txt"

current_date = datetime.now()
current_day = current_date.day
current_month = current_date.month

try:
    df_birthdays = pd.read_csv(BIRTHDAYS_FILE)

except FileNotFoundError:
    print(f"No birthday file ({BIRTHDAYS_FILE}) found.")

else:
    for (_, row) in df_birthdays.iterrows():
        if (current_month == row["month"]) and (current_day == row["day"]):
            try:
                letter_file = LETTER_X_FILE.replace("[X]", str(randint(1, 3)))
                with open(letter_file, "r") as birth_file:
                    birthday_message = birth_file.read()

            except FileNotFoundError:
                print("Format letter was not found.")

            else:
                birthday_message = birthday_message.replace("[NAME]", row["name"])
                with smtplib.SMTP(HOST, PORT) as connection:
                    connection.starttls()
                    connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
                    connection.sendmail(from_addr=SENDER_EMAIL,
                                        to_addrs=row["email"],
                                        msg=f"Subject:Happy Birthday!\n\n{birthday_message}")
