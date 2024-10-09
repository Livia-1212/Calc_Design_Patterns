# main.py
from app.calculator import Calculator
from app.command_handler import CommandHandler
from app.invoker import Invoker
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def interactive_calculator():
    # Initialize the calculator and command handler
    calculator = Calculator()
    command_handler = CommandHandler()

    # Register the commands with the handler
    command_handler.register_command("add", AddCommand(calculator, 0))
    command_handler.register_command("subtract", SubtractCommand(calculator, 0))
    command_handler.register_command("multiply", MultiplyCommand(calculator, 0))
    command_handler.register_command("divide", DivideCommand(calculator, 0))
    command_handler.register_command("reset", lambda: calculator.reset())

    # Create the invoker and pass the command handler to it
    invoker = Invoker(command_handler)


    # Start the REPL loop
    invoker.start_repl()

if __name__ == "__main__":
    interactive_calculator()
