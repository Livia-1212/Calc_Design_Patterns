# plugins/arithmetic/__init__.py

from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def register_commands(command_handler, calculator):
    """Register arithmetic commands with the command handler."""
    command_handler.register_command("add", AddCommand(calculator, 0))
    command_handler.register_command("subtract", SubtractCommand(calculator, 0))
    command_handler.register_command("multiply", MultiplyCommand(calculator, 0))
    command_handler.register_command("divide", DivideCommand(calculator, 0))
