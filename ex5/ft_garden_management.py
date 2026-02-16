class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception for plant-related errors."""
    pass


class WaterError(GardenError):
    """Exception for water-related errors."""
    pass


class Plant:
    """Simple plant object."""
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """
    Manages garden operations such as adding plants,
    watering them, and checking their health.

    Attributes:
        plant1 (Plant or None): First plant slot.
        plant2 (Plant or None): Second plant slot.
        water_tank (int): Available water in the tank.
    """
    def __init__(self):
        self.plant1 = None
        self.plant2 = None
        self.water_tank = 10

    def add_plant(self, name, water, sun):
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        else:
            print(f"Added {name} successfully")
        plant = Plant(name, water, sun)
        if self.plant1 is None:
            self.plant1 = plant
        elif self.plant2 is None:
            self.plant2 = plant
        else:
            return

    def water_plants(self):
        if self.water_tank <= 0:
            raise WaterError("Not enough water in tank")
        else:
            try:
                if self.water_tank <= 0:
                    raise WaterError("Not enough water in tank")
                if self.plant1:
                    print(f"Watering {self.plant1.name} - success")
                    self.water_tank -= 1
                if self.plant2:
                    print(f"Watering {self.plant2.name} - success")
                    self.water_tank -= 1
            except WaterError as e:
                print(f"Caught GardenError: {e}")
            finally:
                print("Closing watering system (cleanup)")

    def check_plant_health(self, plant):
        if plant.water < 1:
            raise WaterError(f"Water level {plant.water} is too low (min 1)")
        elif plant.water > 10:
            raise WaterError(f"Water level {plant.water} is too hi"
                             f"gh (max 10)")
        elif plant.sun < 2:
            raise GardenError(f"Sunlight hours {plant.sun} is "
                              f"too low (min 2)")
        elif plant.sun > 12:
            raise GardenError(f"Sunlight hours {plant.sun} is "
                              f"too high (max 12)")
        else:
            print(f"{plant.name}: healthy (water: {plant.water},"
                  f" sun: {plant.sun})")


def test_garden_management():
    print("=== Garden Management System ===\n")

    garden = GardenManager()
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 15, 6)
        garden.add_plant("", 4, 6)
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    print("Opening watering system")
    garden.water_plants()
    print("\nChecking plant health...")
    try:
        if garden.plant1:
            garden.check_plant_health(garden.plant1)
    except WaterError or GardenError as e:
        print(f"Error checking {garden.plant1.name}: {e}")
    try:
        if garden.plant2:
            garden.check_plant_health(garden.plant2)
    except WaterError or GardenError as e:
        print(f"Error checking {garden.plant2.name}: {e}")
    print("\nTesting error recovery...")
    garden.water_tank = 0
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")
