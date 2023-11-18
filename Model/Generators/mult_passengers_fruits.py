import csv
import random

# Read passenger_airports.csv
passenger_airports_data = []
with open("../../Data/passenger_airports.csv", "r") as f:
    reader = csv.reader(f)
    for row in csv.DictReader(f):
        passenger_airports_data.append(row)

# Read fruit_data.csv
fruit_data = []
with open("../../Data/fruit_data.csv", "r") as f:
    reader = csv.reader(f)
    for row in csv.DictReader(f):
        fruit_data.append(row)

# Multiply passenger and fruit_data
passenger_fruits_data = []
for passenger in passenger_airports_data:
    num_fruits = random.randint(5, 10)
    random_fruits = random.sample(fruit_data, num_fruits)
    passenger_fruits = {
        "ID": passenger["ID"],
        "Name": passenger["Name"],
        "Fruits": [
            {
                "FruitID": fruit["ID"],
                "Fruit": fruit["Fruit"],
                "Score": round(random.uniform(0.0, 5.0), 2),
                "Country": fruit["Country"],
                "From": fruit["Code"],
            }
            for fruit in random_fruits
        ],
    }
    passenger_fruits_data.append(passenger_fruits)

# Print the multiplied data
for passenger in passenger_fruits_data:
    print(f"Name: {passenger['Name']}")
    for fruit in passenger["Fruits"]:
        print(f"Fruit: {fruit['Fruit']}, Score: {fruit['Score']}")
    print()

# Write to passenger_fruits.csv
with open("passenger_fruits.csv", "w") as f:
    f.write("ID,Name,FruitID,Fruit,Score,Country,From\n")
    for passenger in passenger_fruits_data:
        for fruit in passenger["Fruits"]:
            f.write(
                f"{passenger['ID']}, {passenger['Name']},{fruit['FruitID']},{fruit['Fruit']},{fruit['Score']},{fruit['Country']},{fruit['From']}\n"
            )
