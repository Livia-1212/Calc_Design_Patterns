from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Calculator Class (Receiver)
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, amount):
        self.value += amount
        return self.value

    def subtract(self, amount):
        self.value -= amount
        return self.value

    def multiply(self, amount):
        self.value *= amount
        return self.value

    def divide(self, amount):
        if amount != 0:
            self.value /= amount
        else:
            return "Error: Division by zero"
        return self.value
