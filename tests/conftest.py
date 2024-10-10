# tests/conftest.py

import pytest
from app.calculator import Calculator
from app.command_handler import CommandHandler
from app.multiprocess import Invoker
from multiprocessing import Manager  # Import the Manager for shared state
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()

@pytest.fixture
def command_handler(calculator):
    """Fixture to create a CommandHandler linked to a Calculator instance."""
    handler = CommandHandler(calculator)  # Pass the calculator to CommandHandler
    return handler

@pytest.fixture
def calculator_state():
    """Fixture to create a shared calculator state using multiprocessing.Manager."""
    with Manager() as manager:
        state = manager.Namespace()
        state.value = 0  # Initialize calculator value
        yield state

@pytest.fixture
def invoker(command_handler):
    """Fixture to create an Invoker instance linked to the CommandHandler."""
    return Invoker(command_handler)

@pytest.fixture
def add_command(calculator):
    """Fixture to create an AddCommand instance."""
    return AddCommand(calculator, 10)

@pytest.fixture
def subtract_command(calculator):
    """Fixture to create a SubtractCommand instance."""
    return SubtractCommand(calculator, 5)

@pytest.fixture
def multiply_command(calculator):
    """Fixture to create a MultiplyCommand instance."""
    return MultiplyCommand(calculator, 2)

@pytest.fixture
def divide_command(calculator):
    """Fixture to create a DivideCommand instance."""
    return DivideCommand(calculator, 2)
