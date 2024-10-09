# tests/test_invoker.py
import pytest
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_show_menu(capsys, invoker):
    """Test that the menu displays the correct commands."""
    invoker.show_menu()
    captured = capsys.readouterr()
    assert "add <value>" in captured.out
    assert "subtract <value>" in captured.out
    assert "multiply <value>" in captured.out
    assert "divide <value>" in captured.out
    assert "reset" in captured.out
    assert "exit" in captured.out

def test_execute_add_command(calculator, invoker, command_handler):
    """Test that Invoker correctly executes an AddCommand."""
    add_command = AddCommand(calculator, 10)
    command_handler.register_command("add", add_command)
    result = invoker.execute_command("add")
    assert result == 10
    assert calculator.value == 10  # Calculator value should be updated to 10

def test_execute_subtract_command(calculator, invoker, command_handler):
    """Test that Invoker correctly executes a SubtractCommand."""
    # Set initial value to 20 and perform subtraction
    calculator.value = 20
    subtract_command = SubtractCommand(calculator, 5)
    command_handler.register_command("subtract", subtract_command)
    result = invoker.execute_command("subtract")
    assert result == 15
    assert calculator.value == 15  # Calculator value should be updated to 15

def test_execute_multiply_command(calculator, invoker, command_handler):
    """Test that Invoker correctly executes a MultiplyCommand."""
    # Set initial value to 3 and perform multiplication
    calculator.value = 3
    multiply_command = MultiplyCommand(calculator, 4)
    command_handler.register_command("multiply", multiply_command)
    result = invoker.execute_command("multiply")
    assert result == 12
    assert calculator.value == 12  # Calculator value should be updated to 12

def test_execute_divide_command(calculator, invoker, command_handler):
    """Test that Invoker correctly executes a DivideCommand."""
    # Set initial value to 20 and perform division
    calculator.value = 20
    divide_command = DivideCommand(calculator, 4)
    command_handler.register_command("divide", divide_command)
    result = invoker.execute_command("divide")
    assert result == 5
    assert calculator.value == 5  # Calculator value should be updated to 5

def test_execute_divide_by_zero(calculator, invoker, command_handler):
    """Test that Invoker correctly handles division by zero."""
    # Set initial value to 10 and try division by zero
    calculator.value = 10
    divide_command = DivideCommand(calculator, 0)
    command_handler.register_command("divide", divide_command)
    result = invoker.execute_command("divide")
    assert result == "Error: Division by zero"
    assert calculator.value == 10  # Calculator value should remain unchanged

def test_invalid_command(invoker, capsys):
    """Test invalid command handling."""
    invoker.start_repl = lambda: None  # Disable REPL loop for test
    invoker.execute_command("invalid")
    captured = capsys.readouterr()
    assert "Command 'invalid' not found." in captured.out
