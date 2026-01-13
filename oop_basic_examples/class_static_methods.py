class MathUtils:
    # Class-level attribute
    version = "1.0"

    def __init__(self, name="Calculator"):
        self.name = name  # Instance attribute

    # Traditional instance method - operates on instance state
    def greet(self):
        return f"Hello from {self.name}"

    # Static method - pure utility function, no access to instance or class
    @staticmethod
    def add(a, b):
        return a + b

    # Class method - can access and modify class-level data
    @classmethod
    def get_version(cls):
        return f"MathUtils version {cls.version}"

    # Class method - can create instances or modify class behavior
    @classmethod
    def create_default(cls):
        return cls("Default Calculator")

    # Class method - demonstrates class-level operations
    @classmethod
    def update_version(cls, new_version):
        cls.version = new_version
        return f"Version updated to {cls.version}"


# Usage examples to showcase differences
calculator1 = MathUtils("Advanced Calculator")
calculator2 = MathUtils.create_default()

# Instance method - requires instance, operates on instance state
print(calculator1.greet())  # Hello from Advanced Calculator

# Static method - called on class or instance, no access to self/cls
print(MathUtils.add(5, 3))  # 8

# Class method - operates on class level, not instance level
print(MathUtils.get_version())  # MathUtils version 1.0
print(calculator2.get_version())  # MathUtils version 1.0

# Class method can modify class state
print(MathUtils.update_version("2.0"))  # Version updated to 2.0
print(MathUtils.get_version())  # MathUtils version 2.0

# Instance still shows updated class version
print(calculator1.get_version())  # MathUtils version 2.0
