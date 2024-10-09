# tests/test_calculator.py
import pytest
from app.calculator import Calculator

def test_addition(calculator):
    assert calculator.add(10) == 10
    assert calculator.add(5) == 15

def test_subtraction(calculator):
    assert calculator.subtract(5) == -5
    assert calculator.subtract(10) == -15

def test_multiplication(calculator):
    calculator.add(2)  # Set initial value to 2
    assert calculator.multiply(5) == 10

def test_division(calculator):
    calculator.add(10)  # Set initial value to 10
    assert calculator.divide(2) == 5
    assert calculator.divide(0) == "Error: Division by zero"
