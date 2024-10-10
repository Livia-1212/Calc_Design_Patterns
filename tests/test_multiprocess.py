# tests/test_multiprocess.py

import pytest
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_show_menu(capsys, invoker):
    """Test that the menu displays the correct commands."""
    invoker.show_menu()
    captured = capsys.readouterr()
    assert "add <value>" in captured.out
    assert "subtract <value>" in captured.out
    assert "reset" in captured.out
    assert "exit" in captured.out

def test_execute_add_command(calculator, invoker, command_handler, calculator_state):
    """Test that Invoker correctly executes an AddCommand."""
    add_command = AddCommand(calculator, 10)
    command_handler.register_command("add", add_command)
    result = invoker.execute_command("add", calculator_state)
    assert result == 10  # Result should be 10
    assert calculator_state.value == 10  # Calculator state should be updated to 10

def test_execute_command_from_handler(command_handler, calculator, invoker, calculator_state):
    """Test that the command handler correctly executes a registered command."""
    add_command = AddCommand(calculator, 20)
    command_handler.register_command("add", add_command)
    result = invoker.execute_command("add", calculator_state)
    assert result == 20
    assert calculator_state.value == 20

def test_invalid_command(invoker, calculator_state):
    """Test invalid command handling."""
    # Directly call the command to capture the error message
    result = invoker.execute_command("invalid", calculator_state)
    assert result == "Error: Command 'invalid' not found."


def test_execute_subtract_command(calculator, invoker, command_handler, calculator_state):
    """Test that Invoker correctly executes a SubtractCommand."""
    subtract_command = SubtractCommand(calculator, 5)
    command_handler.register_command("subtract", subtract_command)
    result = invoker.execute_command("subtract", calculator_state)
    assert result == -5
    assert calculator_state.value == -5

def test_execute_multiply_command(calculator, invoker, command_handler, calculator_state):
    """Test that Invoker correctly executes a MultiplyCommand."""
    multiply_command = MultiplyCommand(calculator, 2)
    command_handler.register_command("multiply", multiply_command)
    result = invoker.execute_command("multiply", calculator_state)
    assert result == 0  # 0 multiplied by 2 should be 0
    assert calculator_state.value == 0

def test_execute_divide_command(calculator, invoker, command_handler, calculator_state):
    """Test that Invoker correctly executes a DivideCommand."""
    divide_command = DivideCommand(calculator, 2)
    command_handler.register_command("divide", divide_command)
    result = invoker.execute_command("divide", calculator_state)
    assert result == 0  # 0 divided by 2 should be 0
    assert calculator_state.value == 0

def test_execute_divide_by_zero(calculator, invoker, command_handler, calculator_state):
    """Test that Invoker handles divide by zero error."""
    divide_command = DivideCommand(calculator, 0)
    command_handler.register_command("divide", divide_command)
    result = invoker.execute_command("divide", calculator_state)
    assert result is None  # Division by zero should return None
    assert calculator_state.value == 0
