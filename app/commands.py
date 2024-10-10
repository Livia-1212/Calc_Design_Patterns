# command classes to implement interface and execute operations on the Calculator

from abc import ABC, abstractmethod
from app.calculator import Calculator

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class AddCommand(Command):
    def __init__(self, calculator: Calculator, value: float):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.add(self.value)

class SubtractCommand(Command):
    def __init__(self, calculator: Calculator, value: float):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.subtract(self.value)

class MultiplyCommand(Command):
    def __init__(self, calculator: Calculator, value: float):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.multiply(self.value)

class DivideCommand(Command):
    """Command to divide the calculator value by a specified value."""

    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        """Execute the division command and handle division by zero."""
        if self.value == 0:
            print("Error: Division by zero")  # Print error message
            return None  # Return None to indicate an error
        self.calculator.value /= self.value
        return self.calculator.value