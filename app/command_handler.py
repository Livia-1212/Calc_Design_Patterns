# CommandHandler to manage the registration and execution of commands

from app.calculator import Calculator

class CommandHandler:
    def __init__(self, calculator: Calculator):
        """Initialize the command handler with a calculator instance."""
        self.calculator = calculator
        self.commands = {}  # Dictionary to store registered commands

    def register_command(self, command_name, command):
        """Register a new command with a given name."""
        self.commands[command_name] = command

    def execute_command(self, command_name):
        """Execute a registered command by its name."""
        if command_name in self.commands:
            return self.commands[command_name].execute()
        else:
            print(f"Error: Command '{command_name}' not found.")
            return None