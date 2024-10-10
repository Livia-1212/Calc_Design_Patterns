# CommandHandler to manage the registration and execution of commands
import importlib
import pkgutil
import plugins

class CommandHandler:
    def __init__(self, calculator):
        self.commands = {}
        self.calculator = calculator

    def register_command(self, command_name: str, command):
        """Register a new command with the command name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute a registered command by its name."""
        if command_name not in self.commands:
            print(f"Error: Command '{command_name}' not found.")
            return None

        command = self.commands[command_name]
        return command.execute() if hasattr(command, 'execute') else command()

    def load_plugins(self):
        """Dynamically discover and load command plugins from the plugins subfolders."""
        package = plugins

        for _, subpackage_name, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            if ispkg:
                # Import the subpackage (e.g., plugins.arithmetic)
                subpackage = importlib.import_module(subpackage_name)

                # Look for a `register_commands` function in the subpackage's __init__.py
                if hasattr(subpackage, "register_commands"):
                    # Call the registration function with `self` and `self.calculator`
                    register_func = getattr(subpackage, "register_commands")
                    register_func(self, self.calculator)
