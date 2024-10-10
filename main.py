from app.calculator import Calculator
from app.command_handler import CommandHandler
from app.invoker import Invoker
from app.plugin_loader import PluginLoader

def interactive_calculator():
    """Main interactive calculator function."""

    # Initialize the calculator and command handler
    calculator = Calculator()
    command_handler = CommandHandler(calculator)

    # Specify the plugins package to load from
    plugins_package = 'plugins'

    # Load plugins using PluginLoader and pass the calculator instance
    PluginLoader.load_plugins(command_handler, plugins_package, calculator)

    # Create the invoker and pass the command handler to it
    invoker = Invoker(command_handler)

    # Start the REPL loop
    invoker.start_repl()

if __name__ == "__main__":
    interactive_calculator()
