# CommandHandler to manage the registration and execution of commands

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command):
        """Register a new command with the command name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute a registered command by its name."""
        if command_name in self.commands:
            return self.commands[command_name].execute()
        else:
            return f"Command '{command_name}' not found."
