# plugins/reset/__init__.py

from app.commands import Command

class ResetCommand(Command):
    """Command to reset the calculator to zero."""

    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        """Reset the calculator value to zero."""
        self.calculator.value = 0
        return self.calculator.value

def register_commands(command_handler, calculator):
    """Register the reset command with the command handler."""
    command_handler.register_command("reset", ResetCommand(calculator))
