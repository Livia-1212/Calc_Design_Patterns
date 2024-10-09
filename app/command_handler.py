# CommandHandler to manage the registration and execution of commands

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command):
        """Register a new command with the command name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute a registered command by its name."""
        if command_name not in self.commands:
            print(f"Error: Command '{command_name}' not found.")
            return None
        
        command = self.commands[command_name]
        
        # Check if the command is a callable function or a command object
        if callable(command):
            # If the command is a function (like `lambda`), call it directly
            return command()
        elif hasattr(command, 'execute'):
            # If the command is a command object, call its `execute()` method
            return command.execute()
        else:
            print(f"Error: Command '{command_name}' is not executable.")
            return None

