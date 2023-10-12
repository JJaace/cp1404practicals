"""
wimbledon
Estimate: 1 hour
Actual: 2 hours
"""

FILENAME = "wimbledon.csv"


def main():
    data = read_file(FILENAME)
    champions, countries = filter_data(data)
    print_results(champions, countries)


def read_file(filename):
    """This function reads the selected file and returns the data"""

    data = []

    with open(filename, 'r', encoding='utf-8-sig') as file:
        file.readline()
        for row in file:
            data.append(row.strip().split(","))
    return data


def filter_data(data):
    """This function goes through the data and retrieves specific information"""

    champions = {}
    countries = set()

    for row in data:
        champion = row[2]
        country = row[1]
        countries.add(country)

        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1

    return champions, countries


def print_results(champions, countries):
    """This function prints the results"""

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
