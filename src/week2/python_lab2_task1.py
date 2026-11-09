"""
Name-ID: Yusuf Dogukan Dogan - 251ADB239

Lab 2.1 – Simple Datasets and Aggregates
----------------------------------------
Practice lists, dictionaries and tuples by computing simple aggregates.

Write these functions:
- average(values)               -> float
    Average of a list of numbers. Return 0.0 if the list is empty.
- largest_city(populations)     -> tuple (name, population)
    The city with the LARGEST population.
- smallest_city(populations)    -> tuple (name, population)
    The city with the SMALLEST population.
- total_population(populations) -> int
    Sum of all populations. Return 0 if the dict is empty.

`populations` is a dictionary like {"Riga": 605000, "Daugavpils": 78000}.
For largest_city() and smallest_city():
- If two cities tie, return the one that comes FIRST in the dictionary.
- If the dictionary is empty, return ("", 0).
- Built-ins such as sum(), len(), max() and min() are allowed.
  Hint: max(populations, key=populations.get) gives the key with the
  largest value.

In the main block: create your OWN datasets (a list `temperatures` with
7 daily temperatures, and a dict `city_population` with at least 5 cities),
call the functions, and print the results. Print the average with
1 decimal place.

Example run (with your own data the numbers will differ):
    Average temperature: 4.3
    Largest city: Riga - 605000
    Smallest city: Valmiera - 23000
    Total population: 806000

Examples (these are also used to check your work):
>>> average([1, 2, 3, 4])
2.5
>>> average([])
0.0
>>> cities = {"Riga": 605000, "Daugavpils": 78000, "Liepaja": 67000}
>>> largest_city(cities)
('Riga', 605000)
>>> smallest_city(cities)
('Liepaja', 67000)
>>> total_population(cities)
750000
>>> largest_city({})
('', 0)
>>> largest_city({"A": 10, "B": 10})
('A', 10)
"""


def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    city = max(populations, key=lambda k: populations[k])
    return (city, populations[city])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    city = min(populations, key=lambda k: populations[k])
    return (city, populations[city])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    return sum(populations.values())


if __name__ == "__main__":
    temperatures = [4.5, 3.2, 5.1, 6.0, 2.8, 3.5, 5.0]
    city_population = {
        "Istanbul": 15460000,
        "Ankara": 5663000,
        "Izmir": 4367000,
        "Bursa": 3101000,
        "Antalya": 2548000,
    }

    avg_temp = average(temperatures)
    print(f"Average temperature: {avg_temp:.1f}")

    largest_name, largest_pop = largest_city(city_population)
    print(f"Largest city: {largest_name} - {largest_pop}")

    smallest_name, smallest_pop = smallest_city(city_population)
    print(f"Smallest city: {smallest_name} - {smallest_pop}")

    print(f"Total population: {total_population(city_population)}")
