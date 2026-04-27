# Workshop 7 - Why classes? Same problem, two ways.

# Problem: track a small fleet of cars.
# We want to:
#   - store each car's brand, year, and mileage
#   - add a trip (increases mileage)
#   - show a car
#   - find cars older than a given year
#   - get the total mileage of the whole fleet


# ==================================================
# VERSION 1 - WITHOUT classes (dicts + functions)
# ==================================================

# Each car is a dict. The fleet is a list of dicts.
fleet = [
    {"brand": "Toyota", "year": 2018, "mileage": 50000},
    {"brand": "BMW",    "year": 2021, "mileage": 12000},
    {"brand": "Lada",   "year": 2005, "mileage": 230000},
    {"brand": "Mercedes", "year": 2026, "mileage": 17000},
]

def car_add_trip(car, km):
    car["mileage"] += km

def car_show(car):
    print(f"{car['year']} {car['brand']} - {car['mileage']} km")

def fleet_older_than(fleet, year):
    # older_cars = []
    # for car in fleet:
    #     if car["year"] < year:
    #         older_cars.append(car)
    # return older_cars
    return [
        c
        for c in fleet
        if c["year"] < year
    ]

def fleet_total_mileage(fleet):
    return sum(c["mileage"] for c in fleet)


# Use it:
print("--- Without classes ---")
car_add_trip(fleet[0], 250)
car_add_trip(fleet[2], 1000)
car_add_trip(fleet[3], 17)
for car in fleet:
    car_show(car)

print(f"Older than 2010: {fleet_older_than(fleet, 2010)}")
print(f"Total mileage: {fleet_total_mileage(fleet)} km")


# Problems with this approach:
#
# 1. The data and the functions live in different places.
#    "What can I do with a car?" - you have to grep the file for "car_*".
#
# 2. Typos in keys fail silently or much later.
#    car["milage"] += km   # works (creates a new key!) - bug stays hidden
#
# 3. Nothing forces you to provide brand/year/mileage when you create a car.
#    fleet.append({"brand": "Audi"})  # missing fields - crashes later
#
# 4. Function names get long and prefix-y (car_show, fleet_total_mileage)
#    because there's no namespace. The bigger the project, the worse this gets.
#
# 5. Hard to extend. If we want an ElectricCar with a battery percentage,
#    we have to add "if car.get('battery')..." branches everywhere.



# ==================================================
# VERSION 2 - WITH classes
# ==================================================

class Car:
    def __init__(self, brand, year, mileage=0):
        # The constructor REQUIRES brand and year. No "forgot a field" bugs.
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def add_trip(self, km):
        self.mileage += km

    def __repr__(self):
        return f"{self.year} {self.brand} - {self.mileage} km"


class Fleet:
    def __init__(self):
        self.cars = []

    def add(self, car):
        self.cars.append(car)

    def older_than(self, year):
        return [c for c in self.cars if c.year < year]

    def total_mileage(self):
        return sum(c.mileage for c in self.cars)


# Use it:
print("\n--- With classes ---")
fleet2 = Fleet()
fleet2.add(Car("Toyota", 2018, 50000))
fleet2.add(Car("BMW", 2021, 12000))
fleet2.add(Car("Lada", 2005, 230000))

fleet2.cars[0].add_trip(250)
for car in fleet2.cars:
    print(car)
print(f"Older than 2010: {fleet2.older_than(2010)}")
print(f"Total mileage: {fleet2.total_mileage()} km")


# What got better:
#
# 1. Data and behavior live together. "What can a Car do?" -> read the Car class.
#
# 2. Typos fail loudly:
#       car.milage += 100   # AttributeError - immediate, easy to fix
#
# 3. Required fields are enforced by __init__:
#       Car("Audi")         # TypeError: missing 'year'
#
# 4. No name prefixes. car.add_trip(...) instead of car_add_trip(car, ...).
#
# 5. Easy to extend with inheritance. Need an ElectricCar?
#
#       class ElectricCar(Car):
#           def __init__(self, brand, year, battery_kwh, mileage=0):
#               super().__init__(brand, year, mileage)
#               self.battery_kwh = battery_kwh
#
#    All Car methods still work, plus you add new ones for the battery.



# ==================================================
# Rule of thumb
# ==================================================

# Use a class when:
#   - several pieces of data belong together (a car has brand AND year AND mileage)
#   - there are operations that always use that data (add_trip, show, ...)
#   - you'll have many of them and want to treat them uniformly
#
# A plain dict or tuple is fine when:
#   - it's a one-off bag of values
#   - you only pass it around, never operate on it
#   - the structure is genuinely temporary (e.g., a JSON response you read once)
