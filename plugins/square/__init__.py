# plugins/square/__init__.py

from app.commands import Command

class SquareCommand(Command):
    """Command to calculate the square of a value."""

    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        """Calculate the square of the specified value."""
        result = self.value ** 2
        self.calculator.value = result
        return result

def register_commands(command_handler, calculator):
    """Register the square command with the command handler."""
    command_handler.register_command("square", SquareCommand(calculator, 0))
