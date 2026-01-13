class Bird:
    def fly(self):
        return "Flying with wings"


class Airplane:
    def fly(self):
        return "Flying with engines"


class Superman:
    def fly(self):
        return "Flying with superpowers"


# Usage - Duck typing in action
flyers = [Bird(), Airplane(), Superman()]

for flyer in flyers:
    print(flyer.fly())
    # No need to know the actual type, just that it can fly

superman = Superman()
print(isinstance(superman, Bird))
