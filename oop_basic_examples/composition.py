# 5. Composition Example
class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        return self.engine.start()


# Usage
my_car = Car()
print(my_car.start())  # Engine started
