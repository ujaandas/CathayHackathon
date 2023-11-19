import csv
import random

# Read fruit_data.csv
fruit_data = []
with open("../../Data/fruit_data.csv", "r") as f:
    reader = csv.reader(f)
    for row in csv.DictReader(f):
        fruit_data.append(row)

# Read flight_data.csv
flight_data = []
with open("../../Data/flight_data.csv", "r") as f:
    reader = csv.reader(f)
    for row in csv.DictReader(f):
        flight_data.append(row)

# Multiply passenger and fruit_data
flight_fruit_data = []
for fruit in fruit_data:
    num_flights = random.randint(5, 10)
    random_flights = random.sample(flight_data, num_flights)
    flight_fruits = {
        "ID": fruit["ID"],
        "Fruit": fruit["Fruit"],
        "Code": fruit["Code"],
        "Flights": [
            {
                "FlightID": flight["Flight Number"],
                "Arrival Date": flight["Arrival Date"],
                "Via": flight["Via"],
            }
            for flight in random_flights
        ],
    }
    flight_fruit_data.append(flight_fruits)

# Write to flight_fruits.csv
with open("flight_fruits.csv", "w") as f:
    f.write("ID,Fruit,Code,FlightID,Arrival Date,Via\n")
    for fruit in flight_fruit_data:
        for flight in fruit["Flights"]:
            f.write(
                f"{fruit['ID']},{fruit['Fruit']},{fruit['Code']},{flight['FlightID']},{flight['Arrival Date']},{flight['Via']}\n"
            )
