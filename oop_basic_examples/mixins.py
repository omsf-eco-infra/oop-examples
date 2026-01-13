class JSONMixin:
    def to_json(self):
        import json

        return json.dumps(self.__dict__)


class XMLMixin:
    def to_xml(self):
        return f"<{self.__class__.__name__}>{str(self.__dict__)}</{self.__class__.__name__}>"


class Product(JSONMixin, XMLMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Usage
product = Product("Laptop", 999)
print(product.to_json())  # JSON representation
print(product.to_xml())  # XML representation
