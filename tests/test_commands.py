# tests/test_commands.py
import pytest
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command(add_command):
    assert add_command.execute() == 10  # Initial value of calculator is 0 + 10

def test_subtract_command(subtract_command):
    subtract_command.calculator.add(20)  # Set calculator to 20
    assert subtract_command.execute() == 15  # 20 - 5 = 15

def test_multiply_command(multiply_command):
    multiply_command.calculator.add(3)  # Set initial value to 3
    assert multiply_command.execute() == 6  # 3 * 2 = 6

def test_divide_command(divide_command):
    divide_command.calculator.add(10)  # Set initial value to 10
    assert divide_command.execute() == 5  # 10 / 2 = 5

def test_divide_by_zero(calculator):
    divide_command = DivideCommand(calculator, 0)
    assert divide_command.execute() == "Error: Division by zero"
