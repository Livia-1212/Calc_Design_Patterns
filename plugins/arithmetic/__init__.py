# plugins/arithmetic/__init__.py

from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.calculator import Calculator

def register_commands(command_handler, calculator: Calculator):
    """Register arithmetic commands to the command handler."""
    command_handler.register_command("add", AddCommand(calculator, 0))
    command_handler.register_command("subtract", SubtractCommand(calculator, 0))
    command_handler.register_command("multiply", MultiplyCommand(calculator, 0))
    command_handler.register_command("divide", DivideCommand(calculator, 0))

def process_input(command_handler, calculator):
    """Process user input specifically for arithmetic operations."""
    while True:
        user_input = input("Enter arithmetic command: add, subtract, multiply, divide <value>, or 'back' to exit: ").strip().lower()
        
        if user_input == "back":
            print("Exiting arithmetic operations...")
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid format. Use: command <value>")
            continue

        command_name, value_str = parts
        try:
            value = float(value_str)
        except ValueError:
            print("Invalid value. Please enter a numeric value.")
            continue

        # Handle command execution within the plugin itself
        command = command_handler.commands.get(command_name)
        if command:
            command.value = value
            result = command.execute()
            print(f"🧮 Result: {result}")
        else:
            print(f"Unknown command '{command_name}' for arithmetic. Please use: add, subtract, multiply, divide.")
