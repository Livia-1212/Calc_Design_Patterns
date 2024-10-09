import pytest
from app.calculator import Calculator
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.invoker import Invoker

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()

@pytest.fixture
def invoker(calculator):
    """Fixture to create an Invoker instance linked to the Calculator."""
    return Invoker(calculator)

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
