from app.calculator import Command

# Concrete Command Classes
class AddCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.add(self.value)

class SubtractCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.subtract(self.value)

class MultiplyCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.multiply(self.value)

class DivideCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        return self.calculator.divide(self.value)
