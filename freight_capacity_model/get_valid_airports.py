from flight_info import FlightInfo
import requests
import matplotlib.pyplot as plt
from collections import Counter

# Define constants
API_URL = "https://developers.cathaypacific.com/hackathon-apigw/cargo/flights/list"
PAGE_NUM = 0
DATE_FROM = "2023-10-11"
DATE_TO = "2023-11-11"


# Testing params
params = {
    "pageNum": PAGE_NUM,
    "pageSize": 10,
    "userPort": "HKG",
    "depArr": "ARR",
    # YYYY-DD-MM
    "oprDateFrom": DATE_FROM,
    "oprDateTo": DATE_TO,
}

# Headers
headers = {
    "apikey": "hFQl6wL5v3Kx9HM69TUAQxI9AUrr3pyk",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Flight IATAs with cooltainer compatibility
cooltainer_iatas = [
    "74N",  # Boeing 747
    "77W",  # Boeing 777
    "74Y",  # Boeing 747F
]


# Handle response
def handle_response(response, flight_list):
    if response.status_code == 200:
        data = response.json()["data"]
        process_data(data, flight_list)
    else:
        print("Error with API request", response.status_code)


# Updated process_data function to append FlightInfo objects to the provided list
def process_data(data, flight_list):
    for keys in data:
        if can_carry_cooltainers(keys["iataAcType"]):
            # Create new FlightInfo object
            flight = FlightInfo(
                keys["fltNum"],
                keys["fltDate"],
                keys["oprDate"],
                keys["route"],
            )
            flight_list.append(flight)
        else:
            print(f"{keys['iataAcType']} cannot carry cooltainers")


def get_stats(flights, cutoff):
    # Create graph of most visited airports
    visited_airports = [flight.get_visited() for flight in flights]
    visited_airports = [airport for sublist in visited_airports for airport in sublist]
    # Count the occurrences of each airport in the visited_airports list

    airport_counts = Counter(visited_airports)

    # Get the top 10 most visited airports
    top_airports = airport_counts.most_common(cutoff)
    airport_names = [airport[0] for airport in top_airports]
    visit_counts = [airport[1] for airport in top_airports]

    # Calculate the average duration for each airport
    avg_durations = [
        sum(
            flight.get_duration()
            for flight in flights
            if airport in flight.get_visited()
        )
        / airport_counts[airport]
        for airport in airport_names
    ]

    # Create a bar graph to visualize the data
    plt.bar(airport_names, visit_counts)
    plt.xlabel("Airports")
    plt.ylabel("Visit Counts")
    plt.title(f"Top {cutoff} Most Visited Airports")
    plt.xticks(rotation=45)

    # Add average duration above each bar
    for i in range(len(airport_names)):
        plt.text(
            i,
            visit_counts[i] + 0.5,
            f"{avg_durations[i]:.2f} days",
            ha="center",
        )

    # Show the graph
    plt.show()


# Given IATA code, check if aircraft can carry cooltainers
def can_carry_cooltainers(iata_ac_type):
    return iata_ac_type in cooltainer_iatas or not iata_ac_type.startswith("7")


def main():
    # Flight list
    flights = []

    for i in range(10):
        params["pageNum"] = i
        # Make request
        response = requests.get(API_URL, params=params, headers=headers)
        # Handle response
        handle_response(response, flights)

    # Calculate top X most visited airports
    get_stats(flights, 20)


if __name__ == "__main__":
    main()
