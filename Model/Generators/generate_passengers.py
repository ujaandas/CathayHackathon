import random
import requests
import csv

PASSENGER_ID = [
    "510812B00000C8DD",
    "510892B000015B41",
    "510892B00001515E",
    "510892B000015206",
    "510892B0000153AC",
    "510812B00000CADE",
    "510812B00000D1DE",
    "510892B000015CB7",
    "510812B00000D2AF",
    "510812B00000D2D2",
    "510812B00000D2DD",
    "510812B00000D429",
    "510812B00000D429",
    "5109C2B00001E932",
    "5109C2B00001E932",
    "5109C2B00001E6BE",
    "510892B00001634B",
    "510892B00001637F",
    "5109C2B00001E6BE",
    "510892B00001634B",
    "510892B00001637F",
]

# Headers
headers = {
    "apikey": "hFQl6wL5v3Kx9HM69TUAQxI9AUrr3pyk",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}


# Handle response
def handle_response(response, passengers):
    if response.status_code == 200:
        name = get_name(response)
        airports = get_airports(response)
        classes = get_class(response)

        print(f"Name: {name} \nAirports: {airports} \nClasses: {classes} \n\n")
        passengers.append([name, airports, classes])

    else:
        print("Error with API request", response.status_code)


def get_name(response):
    passenger_data = response.json()["data"]["traveler"]
    name = passenger_data["name"]
    # Return formatted name of passenger
    return f"{name['prefix']} {name['firstName']} {name['lastName']}"


def get_airports(response):
    airports = []
    flights_data = response.json()["dictionaries"]["datedFlight"]
    airports = append_airports(flights_data)
    # Return list of airports passenger has visited
    return airports


# Return all airports that the passenger has visited
def append_airports(data):
    airports = []
    for _, flight_details in data.items():
        for flight_point in flight_details["flightPoints"]:
            iata_code = flight_point.get("iataCode")
            if iata_code:
                airports.append(iata_code)
    return airports


def get_class(response):
    classes = []
    class_data = response.json()["included"]

    segment_deliveries = class_data["segmentDeliveries"]

    for _, segment_info in segment_deliveries.items():
        try:
            fare_family_name = segment_info["fareFamilyName"]
            classes.append(fare_family_name)
        except KeyError:
            classes.append(random.choice(["CX-ECONLIGHT", "CX-PEYFLEX", "CX-BIZFLEX"]))

    return classes


# Export data to CSV
def export_to_csv(data):
    with open("passenger_airports.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Visited Airports", "Fare Family"])
        for passenger_data in data:
            user_id = PASSENGER_ID[data.index(passenger_data)]
            name = passenger_data[0]
            airports = ", ".join(passenger_data[1])
            fare_family = passenger_data[2]
            writer.writerow([user_id, name, airports, fare_family])


def main():
    passengers = []
    for passenger_id in PASSENGER_ID:
        API_URL = f"https://developers.cathaypacific.com/hackathon-apigw/airport/customers/{passenger_id}/details"
        response = requests.get(API_URL, headers=headers)
        handle_response(response, passengers)

    export_to_csv(passengers)


if __name__ == "__main__":
    main()
