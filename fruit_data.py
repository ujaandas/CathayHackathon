import random

# Define a dictionary of countries and their associated fruits
country_fruits = {
    "NRT": ["Yuzu", "Persimmon", "Sakura Cherry"],
    "ICN": ["Ginseng", "Korean Pear", "Mandarin Orange"],
    "KIX": ["Kyoho Grapes", "Mikan", "Nashi Pear"],
    "TPE": ["Dragon Fruit", "Lychee", "Papaya"],
    "PVG": ["Longan", "Star Fruit", "Mango"],
    "MNL": ["Mango", "Banana", "Coconut"],
    "PEK": ["Lychee", "Hawthorn", "Peach"],
    "SIN": ["Durian", "Rambutan", "Mangosteen"],
    "BKK": ["Mangosteen", "Pomelo", "Dragon Fruit"],
    "DEL": ["Mango", "Guava", "Pomegranate"],
    "JFK": ["Apple", "Blueberries", "Strawberries"],
    "LAX": ["Avocado", "Orange", "Lemon"],
    "LHR": ["Apple", "Blackcurrant", "Raspberry"],
    "PEN": ["Durian", "Banana", "Pineapple"],
    "CEB": ["Mango", "Papaya", "Jackfruit"],
    "NGO": ["Mikan", "Melon", "Peach"],
    "DAC": ["Lychee", "Guava", "Papaya"],
    "HAN": ["Dragon Fruit", "Mango", "Pomelo"],
    "SYD": ["Kangaroo Paw", "Macadamia Nut", "Quandong"],
    "MEL": ["Kangaroo Apple", "Finger Lime", "Davidsons Plum"],
    "ANC": ["Salmonberry", "Fireweed", "Cloudberry"],
    "HND": ["Mikan", "Peach", "Persimmon"],
    "CGK": ["Durian", "Mango", "Salak"],
    "XMN": ["Lychee", "Pomelo", "Longan"],
    "KHH": ["Pineapple", "Banana", "Wax Apple"],
    "CTU": ["Kiwi", "Peach", "Pomegranate"],
    "SGN": ["Dragon Fruit", "Mango", "Custard Apple"],
    "WTB": ["Durian", "Mango", "Mangosteen"],
    "ORD": ["Apple", "Blueberries", "Strawberries"],
    "CKG": ["Lychee", "Mango", "Pomelo"],
}

# Define the number of mock fruit entries you want
num_entries = 50

# Generate mock fruit data
mock_fruit_data = []
for _ in range(num_entries):
    country = random.choice(list(country_fruits.keys()))
    fruit = random.choice(country_fruits[country])
    rating = random.randint(1, 5)

    # Create a mock fruit entry as a dictionary
    fruit_entry = {"country": country, "fruit": fruit, "rating": rating}

    mock_fruit_data.append(fruit_entry)

# Print the mock fruit data
for entry in mock_fruit_data:
    print(entry)
