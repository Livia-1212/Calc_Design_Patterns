# plugins/exponent/__init__.py

from app.commands import Command

class ExponentCommand(Command):
    """Command to calculate base raised to the power of exponent."""

    def __init__(self, calculator, base, exponent):
        self.calculator = calculator
        self.base = base
        self.exponent = exponent

    def execute(self):
        """Calculate base raised to the power of exponent."""
        result = self.base ** self.exponent
        self.calculator.value = result
        return result

def register_commands(command_handler, calculator):
    """Register the exponent command with the command handler."""
    command_handler.register_command("exponent", ExponentCommand(calculator, 0, 0))
