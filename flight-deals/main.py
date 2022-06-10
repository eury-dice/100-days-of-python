# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

fs = FlightSearch()
dm = DataManager()
sheet_data = dm.get_dest()

need_update = False
for row in sheet_data:
    if row["iataCode"] == "":
        need_update = True
        row["iataCode"] = fs.search_iata(row["city"])

if need_update:
    dm.update_dest(sheet_data)

# # For checking purposes
# print(sheet_data)

tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
date_6_months_later = (datetime.today() + timedelta(days=180)).strftime("%d/%m/%Y")

users = dm.get_users()
for row in sheet_data:
    result = fs.search_flights(destination_location=row["iataCode"],
                               date_from=tomorrow,
                               date_to=date_6_months_later
    )
    if result is None:
        continue
    elif row["lowestPrice"] > result.price:
        nm = NotificationManager(result)
        # nm.send_message()
        nm.send_emails(users)
