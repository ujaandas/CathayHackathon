import random
import requests

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

# Constant API URL
API_URL = f"https://developers.cathaypacific.com/hackathon-apigw/airport/customers/{random.choice(PASSENGER_ID)}/details"

# Headers
headers = {
    "apikey": "hFQl6wL5v3Kx9HM69TUAQxI9AUrr3pyk",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}


# Handle response
def handle_response(response, airports):
    if response.status_code == 200:
        passenger_data = response.json()["data"]["traveler"]
        flights_data = response.json()["dictionaries"]["datedFlight"]
        name = passenger_data["name"]
        print(f"{name['prefix']} {name['firstName']} {name['lastName']} has been to:")
        airports = append_airports(flights_data, airports)
    else:
        print("Error with API request", response.status_code)


# Return all airports that the passenger has visited
def append_airports(data, airports):
    for _, flight_details in data.items():
        for flight_point in flight_details["flightPoints"]:
            iata_code = flight_point.get("iataCode")
            if iata_code:
                airports.append(iata_code)


def main():
    airports = []
    response = requests.get(API_URL, headers=headers)
    handle_response(response, airports)
    print(airports)


if __name__ == "__main__":
    main()
