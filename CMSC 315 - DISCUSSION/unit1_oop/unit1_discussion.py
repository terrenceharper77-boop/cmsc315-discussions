"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Vehicle:
    # class variables
    default_fuel_type= "Gasoline"
    engine_is_on = False

    # constructor with 2 instance variables
    def __init__(self,brand,model):
        self.brand = brand
        self.model= model

    # methods that return or display information

    # returns fuel type
    def get_fuel_type(self):
        return f"The fuel type is {self.default_fuel_type}."

    #toggles engine to start
    def engine_toggle(self):
        #check if engine is on
        if not self.engine_is_on:
            self.engine_is_on = True
            return f"The {self.brand} {self.model}'s is now ON"

        else:
            # if engine is on then turn it off
            if self.engine_is_on:
                self.engine_is_on= False
            return f"The {self.brand} {self.model} is turned off"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#zxc
# Replace the pass statement with your implementation.

class ElectricCar(Vehicle):
    # new class variable
    solar_charging_feature = True

    #constructoe with super usage and 2 new instance variables
    def __init__(self,brand, model, battery_capacity, range_miles):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
        self.range_miles = range_miles

   #override
    def get_fuel_type(self):
        default_fuel_type = "Electric"
        return f"The fuel type is {default_fuel_type}"

   #charge vehicle
    def charge_battery(self, hours):
        # if vehicle has solar charging then use soalr charging
        if not self.solar_charging_feature:
            return f"charging {self.brand}{self.model}for {hours}'s"
        else:
            print("Solar charging activating...")
            return f"Solar charging is active: {self.solar_charging_feature}"

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
     print("\n=== Namespace Demonstration ===")

     # - Create at least two objects of the child class.
     car1 = ElectricCar("Tesla","Model S", 100, 450)
     car2 = ElectricCar("icon","Model T", 100, 500)

     # - Access a class variable through the class itself
     print(f"Printintg Default fuel type for vehicle:{Vehicle.default_fuel_type}")
     # - Access same class varible through an object
     print(f"Printing fuel type for ElectricCar: {ElectricCar.default_fuel_type}")

     # - Add new attribute to only one object after its created
     car2.has_fast_charging = True

     # - Display each object's namespace using __dict__
     # Note how car1's dictionary contains 'is_self_driving', but car2's does not!
     print("\n--- Object 1 Namespace (__dict__) ---")
     print(car1.__dict__)

     print("\n--- Object 2 Namespace (__dict__) ---")
     print(car2.__dict__)

     # Display information about the class namespace
     print ("\n--- class namespace info for Vehicle ---")
     for key, value in Vehicle.__dict__.items():
         if not key.startswith("__"):
             if callable(value):
                 # it's a method -- call it on a sample instance to show
                 # the actual return value instead of a memory address
                 print(f"{key}: {value(car1)}")
             else:
                 print(f"{key}: {value}")
        
# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")


    original= ElectricCar("Nissan", "leaf", 62, 215)
    original.accessories = ["floor mats","high end alloy wheels"]

    #still points to same list
    shallow = copy(original)

    # deepcopy: creates a new object and new copies of attributes
    #no memory shared
    deep = deepcopy(original)

    #modify original nested data
    original.accessories.append("roof rack")
    original.brand = "Cyber"

    print("Original class (Modified): ", original.brand, original.accessories)
    print("Shallow copy: ", shallow.brand, shallow.accessories)
    print("Deep copy: ", deep.brand, deep.accessories)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # parent class object
    car = Vehicle("Nissan", "altima")
    print("\n---parent object---")
    print(car.get_fuel_type())
    print(car.engine_toggle())
    print(car.engine_toggle())

    # chold classs object demonstrating inheritance
    e_car = ElectricCar("Tesla", "Model T",75 , 358)
    print("\n ---child objecct---")
    print(e_car.get_fuel_type()) #overridden
    print(e_car.engine_toggle()) #inheritance
    print(e_car.engine_toggle())
    print(e_car.charge_battery(3)) #new method


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()