# Relationship between Object, Instance, and Class

# 1. Class Definition
# This is the blueprint/template
class Car:
    # Class attribute (shared by all instances)
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes (unique to each object)
        self.make = make
        self.model = model

    def drive(self):
        return f"{self.make} {self.model} is driving"


# 2. Creating Instances (Objects)
# Each instance is a separate object with its own state
car1 = Car("Toyota", "Camry")  # First object/instance
car2 = Car("Honda", "Civic")  # Second object/instance


# 3. Demonstrating the Relationship
print("=== CLASS ===")
print(f"Class name: {Car.__name__}")
print(f"Class attributes: {Car.__dict__}")
print(f"Class has wheels attribute: {hasattr(Car, 'wheels')}")  # True
print(f"Class wheels value: {Car.wheels}")

print("\n=== INSTANCE 1 (car1) ===")
print(f"Instance type: {type(car1)}")
print(f"Instance is Car: {isinstance(car1, Car)}")  # True
print(f"Instance attributes: {car1.__dict__}")
print(f"Instance make: {car1.make}")
print(f"Instance model: {car1.model}")
print(f"Instance wheels: {car1.wheels}")  # Inherited from class

print("\n=== INSTANCE 2 (car2) ===")
print(f"Instance type: {type(car2)}")
print(f"Instance is Car: {isinstance(car2, Car)}")  # True
print(f"Instance attributes: {car2.__dict__}")
print(f"Instance make: {car2.make}")
print(f"Instance model: {car2.model}")
print(f"Instance wheels: {car2.wheels}")  # Inherited from class


# 4. Modifying Class vs Instance
print("\n=== MODIFYING CLASS ATTRIBUTE ===")
Car.wheels = 6  # Change class attribute
print(f"Updated class wheels: {Car.wheels}")
print(f"car1 wheels: {car1.wheels}")  # Updated (inherits from class)
print(f"car2 wheels: {car2.wheels}")  # Updated (inherits from class)

print("\n=== MODIFYING INSTANCE ATTRIBUTE ===")
car1.make = "Ford"  # Change instance attribute
print(f"car1 make: {car1.make}")  # Changed
print(f"car2 make: {car2.make}")  # Unchanged (different instance)

print("\n=== CREATING NEW INSTANCE AFTER CHANGE ===")
car3 = Car("Tesla", "Model 3")
print(f"car3 wheels: {car3.wheels}")  # Inherits updated class value
print(f"car3 make: {car3.make}")  # New instance with default values


# 5. Key Takeaways
print("\n=== RELATIONSHIP SUMMARY ===")
print("• Class: Blueprint/Template")
print("• Instance: Concrete object created from the class")
print("• Object: Another term for instance - they're the same thing")
print("• Instances share class attributes but have their own instance attributes")
print("• Changes to class affect all existing and future instances")
print("• Changes to instance only affect that specific object")
