class Superhero:
    def __init__(self, name, superpower, strength_level):
        """Initialize a superhero with a name, superpower, and strength level."""
        self.name = name
        self.superpower = superpower
        self.strength_level = strength_level  # Private attribute to demonstrate encapsulation
    
    def use_power(self):
        """Demonstrate the superhero using their power."""
        print(f"{self.name} uses their {self.superpower}!")
    
    def get_strength_level(self):
        """Accessor method for the strength level."""
        return self.strength_level
    
    def set_strength_level(self, new_level):
        """Mutator method to update the strength level."""
        if new_level > 0:
            self.strength_level = new_level
        else:
            print("Strength level must be positive.")


# Subclass with an extra layer of specialization
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, strength_level, flight_speed):
        super().__init__(name, superpower, strength_level)
        self.flight_speed = flight_speed  # Unique attribute for flying superheroes
    
    def use_power(self):
        """Override use_power to include flying."""
        print(f"{self.name} flies at {self.flight_speed} mph while using {self.superpower}!")


# Testing the Superhero class
hero1 = Superhero("Shadow", "Invisibility", 80)
hero2 = FlyingSuperhero("Skyhawk", "Wind Manipulation", 100, 200)

hero1.use_power()
print(f"{hero1.name}'s strength level: {hero1.get_strength_level()}")
hero2.use_power()


# Base class for Vehicles
class Vehicle:
    def move(self):
        """Generic move method, intended to be overridden."""
        pass


# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")


# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
