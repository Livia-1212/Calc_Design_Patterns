# plugins/exponent/__init__.py

from app.commands import Command
from app.calculator import Calculator

class ExponentCommand(Command):
    """Command to calculate the exponent of a base value."""
    def __init__(self, calculator: Calculator, base: float, exponent: float):
        self.calculator = calculator
        self.base = base
        self.exponent = exponent

    def execute(self):
        """Calculate and return base raised to the power of exponent."""
        result = self.base ** self.exponent
        return f"Result of {self.base}^{self.exponent} = {result}"

def register_commands(command_handler, calculator):
    """Register the exponent command."""
    command_handler.register_command("exponent", ExponentCommand(calculator, 0, 0))

def process_input(command_handler, calculator):
    """Process user input specifically for exponent operations."""
    while True:
        user_input = input("Enter exponent command: exponent <base> <exponent>, or 'back' to exit: ").strip().lower()

        if user_input == "back":
            print("Exiting exponent operations...")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format. Use: exponent <base> <exponent>")
            continue

        _, base_str, exponent_str = parts
        try:
            base = float(base_str)
            exponent = float(exponent_str)
        except ValueError:
            print("Invalid values. Please enter numeric values for base and exponent.")
            continue

        # Handle exponent command execution within the plugin
        command = command_handler.commands.get("exponent")
        if command:
            command.base = base
            command.exponent = exponent
            result = command.execute()
            print(f"🧮 Result: {result}")
        else:
            print(f"Error: Command 'exponent' is not registered.")
