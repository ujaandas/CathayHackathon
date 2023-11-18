from datetime import datetime


class FlightInfo:
    # Constructor
    def __init__(self, flight_number, departure_time, arrival_time, via_airports):
        self.flight_number = flight_number
        self.departure_time = datetime.strptime(departure_time, "%Y-%m-%d").date()
        self.arrival_time = datetime.strptime(arrival_time, "%Y-%m-%d").date()
        self.via_airports = via_airports.split("/")[:-1]
        self.calculate_duration()

    # Calculate duration of flight
    def calculate_duration(self):
        self.duration = self.arrival_time - self.departure_time

    # Get visited
    def get_visited(self) -> list[str]:
        return self.via_airports

    # Get duration
    def get_duration(self) -> int:
        return self.duration.days

    # String representation
    def __str__(self):
        return f"Flt num: {self.flight_number}, Dep: {self.departure_time}, Arr: {self.arrival_time}, Via: {self.via_airports}, Duration: {self.duration.days} days"
