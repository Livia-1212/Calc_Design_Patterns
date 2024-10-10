# plugins/square/__init__.py

from app.commands import Command
from app.calculator import Calculator

class SquareCommand(Command):
    """Command to calculate the square of a given value."""
    def __init__(self, calculator: Calculator, value: float):
        self.calculator = calculator
        self.value = value

    def execute(self):
        """Calculate and return the square of the given value."""
        result = self.value ** 2
        return f"Result of {self.value}^2 = {result}"

def register_commands(command_handler, calculator):
    """Register the square command with the command handler."""
    command_handler.register_command("square", SquareCommand(calculator, 0))
