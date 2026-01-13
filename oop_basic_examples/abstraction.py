# 4. Abstraction Example
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via credit card")
        return True


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")
        return True


# Usage
processors = [CreditCardProcessor(), PayPalProcessor()]
for processor in processors:
    processor.process_payment(100)
