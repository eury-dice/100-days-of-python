class FlightData:
    def __init__(self, price, depart_city, depart_airport, arrival_city, arrival_airport, outbound_date, inbound_date,
                 stop_overs=0, via_city=""):
        self.price = price
        self.depart_city = depart_city
        self.depart_airport = depart_airport
        self.arrival_city = arrival_city
        self.arrival_airport = arrival_airport
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.stop_overs = stop_overs
        self.via_city = via_city

    # For checking purposes
    def to_string(self):
        return f"{self.depart_city} -> {self.arrival_city}: {self.price} " \
               f"from {self.outbound_date} to {self.inbound_date}\n" \
               f"{self.stop_overs} stop over at {self.via_city}"
