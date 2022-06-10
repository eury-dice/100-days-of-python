import os
import smtplib
from twilio.rest import Client
from flight_data import FlightData

# CONSTANTS
ACCOUNT_SSID = os.environ["TWILIO_SSID"]
AUTH_TOKEN = os.environ["TWILIO_TOKEN"]
SENDER = os.environ["SENDER"]
RECEIVER = os.environ["RECEIVER"]
HOST = os.environ["HOST"]
PORT = os.environ["PORT"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDER_PASS = os.environ["SENDER_PASS"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, fd: FlightData):
        self.client = Client(ACCOUNT_SSID, AUTH_TOKEN)
        self.message = f"Low price alert! Only £{fd.price} to fly from {fd.depart_city}-{fd.depart_airport} to " \
                       f"{fd.arrival_city}-{fd.arrival_airport}, from {fd.outbound_date} to {fd.inbound_date}."

        if fd.stop_overs > 0:
            self.message += f"\nFlight has {fd.stop_overs} stop over via {fd.via_city}."

        self.message += f"\nhttps://www.google.co.uk/flights?hl=en#flt=" \
                        f"{fd.depart_airport}.{fd.arrival_airport}.{fd.outbound_date}*" \
                        f"{fd.arrival_airport}.{fd.depart_airport}.{fd.inbound_date}"

    def send_sms(self):
        result = self.client.messages.create(
            body=self.message,
            from_=SENDER,
            to=RECEIVER
        )
        print(result.status)

    def send_emails(self, users: list):
        for user in users:
            with smtplib.SMTP(HOST, PORT) as connection:
                connection.starttls()
                connection.login(SENDER_EMAIL, SENDER_PASS)
                connection.sendmail(from_addr=SENDER_EMAIL,
                                    to_addrs=user["email"],
                                    msg=f"From: {SENDER_EMAIL}\n"
                                        f"To: {user['email']} \n"
                                        f"Subject:New Low Price Flight\n\n"
                                        f"{self.message}".encode("utf-8"))
