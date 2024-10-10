# plugins/reset/__init__.py

from app.calculator import Calculator
from app.commands import Command

class ResetCommand(Command):
    """Command to reset the calculator's value to zero."""
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self):
        return self.calculator.reset()

def register_commands(command_handler, calculator):
    """Register the reset command to the command handler."""
    command_handler.register_command("reset", ResetCommand(calculator))
