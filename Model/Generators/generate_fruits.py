from Fruit import Country


# Iterate through countries and print countries with no fruits
def check_empty(countries):
    for code, country in countries.items():
        if len(country.fruits) == 0:
            print(f"{country.name} ({code}) has no fruits")


# Iterate through countries and print countries with 2 or less fruits
def check_less(countries):
    for code, country in countries.items():
        if len(country.fruits) <= 2:
            print(f"{country.name} ({code}) has {len(country.fruits)} fruits")


# Export to .csv
def export_to_csv(countries):
    with open("fruit_data.csv", "w") as f:
        f.write("ID,Country,Code,Fruit,Season\n")
        for code, country in countries.items():
            for fruit in country.fruits:
                f.write(
                    f"{fruit.id},{country.name},{code},{fruit.name},{fruit.season}\n"
                )


def main():
    countries = {
        "NRT": Country("NRT", "Japan"),
        "ICN": Country("ICN", "South Korea"),
        "KIX": Country("KIX", "Japan"),
        "TPE": Country("TPE", "Taiwan"),
        "PVG": Country("PVG", "China"),
        "MNL": Country("MNL", "Philippines"),
        "PEK": Country("PEK", "China"),
        "SIN": Country("SIN", "Singapore"),
        "BKK": Country("BKK", "Thailand"),
        "DEL": Country("DEL", "India"),
        "JFK": Country("JFK", "United States"),
        "LAX": Country("LAX", "United States"),
        "LHR": Country("LHR", "United Kingdom"),
        "PEN": Country("PEN", "Malaysia"),
        "CEB": Country("CEB", "Philippines"),
        "NGO": Country("NGO", "Japan"),
        "DAC": Country("DAC", "Bangladesh"),
        "HAN": Country("HAN", "Vietnam"),
        "SYD": Country("SYD", "Australia"),
        "MEL": Country("MEL", "Australia"),
        "ANC": Country("ANC", "United States"),
        "HND": Country("HND", "Japan"),
        "CGK": Country("CGK", "Indonesia"),
        "XMN": Country("XMN", "China"),
        "KHH": Country("KHH", "Taiwan"),
        "CTU": Country("CTU", "China"),
        "SGN": Country("SGN", "Vietnam"),
        "WTB": Country("WTB", "Indonesia"),
        "ORD": Country("ORD", "United States"),
        "CKG": Country("CKG", "China"),
    }

    fruit_id = 0

    # Add fruits to countries
    countries["NRT"].add_fruit("Yuzu", "Winter", fruit_id)
    fruit_id += 1
    countries["NRT"].add_fruit("Persimmon", "Autumn", fruit_id)
    fruit_id += 1
    countries["NRT"].add_fruit("Sakura Cherry", "Spring", fruit_id)
    fruit_id += 1

    countries["ICN"].add_fruit("Ginseng", "All Year", fruit_id)
    fruit_id += 1
    countries["ICN"].add_fruit("Korean Pear", "Autumn", fruit_id)
    fruit_id += 1
    countries["ICN"].add_fruit("Mandarin Orange", "Winter", fruit_id)
    fruit_id += 1

    countries["KIX"].add_fruit("Kyoho Grapes", "Summer", fruit_id)
    fruit_id += 1
    countries["KIX"].add_fruit("Mikan", "Winter", fruit_id)
    fruit_id += 1
    countries["KIX"].add_fruit("Nashi Pear", "Autumn", fruit_id)
    fruit_id += 1

    countries["TPE"].add_fruit("Dragon Fruit", "Summer", fruit_id)
    fruit_id += 1
    countries["TPE"].add_fruit("Lychee", "Summer", fruit_id)
    fruit_id += 1
    countries["TPE"].add_fruit("Papaya", "All Year", fruit_id)
    fruit_id += 1

    countries["PVG"].add_fruit("Longan", "Summer", fruit_id)
    fruit_id += 1
    countries["PVG"].add_fruit("Star Fruit", "Summer", fruit_id)
    fruit_id += 1
    countries["PVG"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1

    countries["MNL"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["MNL"].add_fruit("Banana", "All Year", fruit_id)
    fruit_id += 1
    countries["MNL"].add_fruit("Coconut", "All Year", fruit_id)
    fruit_id += 1

    countries["PEK"].add_fruit("Lychee", "Summer", fruit_id)
    fruit_id += 1
    countries["PEK"].add_fruit("Hawthorn", "Autumn", fruit_id)
    fruit_id += 1
    countries["PEK"].add_fruit("Peach", "Summer", fruit_id)
    fruit_id += 1

    countries["SIN"].add_fruit("Durian", "Summer", fruit_id)
    fruit_id += 1
    countries["SIN"].add_fruit("Rambutan", "Summer", fruit_id)
    fruit_id += 1
    countries["SIN"].add_fruit("Mangosteen", "Summer", fruit_id)
    fruit_id += 1

    countries["BKK"].add_fruit("Mangosteen", "Summer", fruit_id)
    fruit_id += 1
    countries["BKK"].add_fruit("Pomelo", "Winter", fruit_id)
    fruit_id += 1
    countries["BKK"].add_fruit("Dragon Fruit", "Summer", fruit_id)
    fruit_id += 1

    countries["DEL"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["DEL"].add_fruit("Guava", "All Year", fruit_id)
    fruit_id += 1
    countries["DEL"].add_fruit("Pomegranate", "Autumn", fruit_id)
    fruit_id += 1

    countries["JFK"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["JFK"].add_fruit("Blueberries", "Summer", fruit_id)
    fruit_id += 1
    countries["JFK"].add_fruit("Cranberries", "Autumn", fruit_id)
    fruit_id += 1

    countries["XMN"].add_fruit("Longan", "Summer", fruit_id)
    fruit_id += 1
    countries["XMN"].add_fruit("Pomelo", "Winter", fruit_id)
    fruit_id += 1
    countries["XMN"].add_fruit("Lychee", "Summer", fruit_id)
    fruit_id += 1

    countries["KHH"].add_fruit("Pineapple", "All Year", fruit_id)
    fruit_id += 1
    countries["KHH"].add_fruit("Guava", "Summer", fruit_id)
    fruit_id += 1
    countries["KHH"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1

    countries["CTU"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["CTU"].add_fruit("Pear", "Autumn", fruit_id)
    fruit_id += 1
    countries["CTU"].add_fruit("Jujube", "Autumn", fruit_id)
    fruit_id += 1

    countries["SGN"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["SGN"].add_fruit("Dragon Fruit", "Summer", fruit_id)
    fruit_id += 1
    countries["SGN"].add_fruit("Lychee", "Summer", fruit_id)
    fruit_id += 1

    countries["WTB"].add_fruit("Durian", "Summer", fruit_id)
    fruit_id += 1
    countries["WTB"].add_fruit("Mangosteen", "Summer", fruit_id)
    fruit_id += 1
    countries["WTB"].add_fruit("Papaya", "All Year", fruit_id)
    fruit_id += 1

    countries["ORD"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["ORD"].add_fruit("Blueberry", "Summer", fruit_id)
    fruit_id += 1
    countries["ORD"].add_fruit("Cranberry", "Autumn", fruit_id)
    fruit_id += 1

    countries["CKG"].add_fruit("Strawberry", "Spring", fruit_id)
    fruit_id += 1
    countries["CKG"].add_fruit("Avocado", "Summer", fruit_id)
    fruit_id += 1
    countries["CKG"].add_fruit("Lemon", "All Year", fruit_id)
    fruit_id += 1

    countries["KIX"].add_fruit("Persimmon", "Autumn", fruit_id)
    fruit_id += 1
    countries["KIX"].add_fruit("Yuzu", "Winter", fruit_id)
    fruit_id += 1
    countries["KIX"].add_fruit("Sakura Cherry", "Spring", fruit_id)
    fruit_id += 1

    countries["TPE"].add_fruit("Pineapple", "All Year", fruit_id)
    fruit_id += 1
    countries["TPE"].add_fruit("Guava", "Summer", fruit_id)
    fruit_id += 1
    countries["TPE"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1

    countries["PVG"].add_fruit("Lychee", "Summer", fruit_id)
    fruit_id += 1
    countries["PVG"].add_fruit("Dragon Fruit", "Summer", fruit_id)
    fruit_id += 1
    countries["PVG"].add_fruit("Longan", "Summer", fruit_id)
    fruit_id += 1

    countries["MNL"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["MNL"].add_fruit("Banana", "All Year", fruit_id)
    fruit_id += 1
    countries["MNL"].add_fruit("Coconut", "All Year", fruit_id)
    fruit_id += 1

    countries["PEK"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["PEK"].add_fruit("Pear", "Autumn", fruit_id)
    fruit_id += 1
    countries["PEK"].add_fruit("Jujube", "Autumn", fruit_id)
    fruit_id += 1

    countries["SIN"].add_fruit("Durian", "Summer", fruit_id)
    fruit_id += 1
    countries["SIN"].add_fruit("Mangosteen", "Summer", fruit_id)
    fruit_id += 1
    countries["SIN"].add_fruit("Rambutan", "Summer", fruit_id)
    fruit_id += 1

    countries["BKK"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["BKK"].add_fruit("Durian", "Summer", fruit_id)
    fruit_id += 1
    countries["BKK"].add_fruit("Pomelo", "Winter", fruit_id)
    fruit_id += 1

    countries["DEL"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["DEL"].add_fruit("Guava", "Summer", fruit_id)
    fruit_id += 1
    countries["DEL"].add_fruit("Pomegranate", "Autumn", fruit_id)
    fruit_id += 1

    countries["JFK"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["JFK"].add_fruit("Blueberry", "Summer", fruit_id)
    fruit_id += 1
    countries["JFK"].add_fruit("Cranberry", "Autumn", fruit_id)
    fruit_id += 1

    countries["LAX"].add_fruit("Strawberry", "Spring", fruit_id)
    fruit_id += 1
    countries["LAX"].add_fruit("Avocado", "Summer", fruit_id)
    fruit_id += 1
    countries["LAX"].add_fruit("Lemon", "All Year", fruit_id)
    fruit_id += 1

    countries["LHR"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["LHR"].add_fruit("Blackberry", "Summer", fruit_id)
    fruit_id += 1
    countries["LHR"].add_fruit("Raspberry", "Summer", fruit_id)
    fruit_id += 1

    countries["PEN"].add_fruit("Durian", "Summer", fruit_id)
    fruit_id += 1
    countries["PEN"].add_fruit("Mangosteen", "Summer", fruit_id)
    fruit_id += 1
    countries["PEN"].add_fruit("Papaya", "All Year", fruit_id)
    fruit_id += 1

    countries["CEB"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["CEB"].add_fruit("Coconut", "All Year", fruit_id)
    fruit_id += 1
    countries["CEB"].add_fruit("Pineapple", "All Year", fruit_id)
    fruit_id += 1

    countries["NGO"].add_fruit("Peach", "Summer", fruit_id)
    fruit_id += 1
    countries["NGO"].add_fruit("Plum", "Summer", fruit_id)
    fruit_id += 1
    countries["NGO"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1

    countries["DAC"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["DAC"].add_fruit("Jackfruit", "Summer", fruit_id)
    fruit_id += 1
    countries["DAC"].add_fruit("Pineapple", "All Year", fruit_id)
    fruit_id += 1

    countries["HAN"].add_fruit("Mango", "Summer", fruit_id)
    fruit_id += 1
    countries["HAN"].add_fruit("Longan", "Summer", fruit_id)
    fruit_id += 1
    countries["HAN"].add_fruit("Lychee", "Summer", fruit_id)
    fruit_id += 1

    countries["SYD"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1
    countries["SYD"].add_fruit("Orange", "Winter", fruit_id)
    fruit_id += 1
    countries["SYD"].add_fruit("Kiwi", "Winter", fruit_id)
    fruit_id += 1

    countries["MEL"].add_fruit("Cherry", "Spring", fruit_id)
    fruit_id += 1
    countries["MEL"].add_fruit("Plum", "Summer", fruit_id)
    fruit_id += 1
    countries["MEL"].add_fruit("Apricot", "Spring", fruit_id)
    fruit_id += 1

    countries["ANC"].add_fruit("Blueberry", "Summer", fruit_id)
    fruit_id += 1
    countries["ANC"].add_fruit("Raspberry", "Summer", fruit_id)
    fruit_id += 1
    countries["ANC"].add_fruit("Strawberry", "Spring", fruit_id)
    fruit_id += 1

    countries["HND"].add_fruit("Peach", "Summer", fruit_id)
    fruit_id += 1
    countries["HND"].add_fruit("Plum", "Summer", fruit_id)
    fruit_id += 1
    countries["HND"].add_fruit("Apple", "Autumn", fruit_id)
    fruit_id += 1

    countries["CGK"].add_fruit("Durian", "Summer", fruit_id)
    fruit_id += 1
    countries["CGK"].add_fruit("Mangosteen", "Summer", fruit_id)
    fruit_id += 1
    countries["CGK"].add_fruit("Papaya", "All Year", fruit_id)
    fruit_id += 1

    export_to_csv(countries)


if __name__ == "__main__":
    main()
