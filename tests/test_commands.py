# Verify that the command classes work as expected
def test_add_command(add_command):
    assert add_command.execute() == 10  # Initial value 0 + 10

def test_subtract_command(subtract_command, calculator):
    calculator.add(20)  # Set calculator value to 20
    assert subtract_command.execute() == 15  # 20 - 5 = 15

def test_multiply_command(multiply_command, calculator):
    calculator.add(3)  # Set calculator value to 3
    assert multiply_command.execute() == 6  # 3 * 2 = 6

def test_divide_command(divide_command, calculator):
    calculator.add(10)  # Set calculator value to 10
    assert divide_command.execute() == 5  # 10 / 2 = 5

def test_divide_by_zero(divide_command):
    divide_command.value = 0  # Change divide value to zero
    assert divide_command.execute() == "Error: Division by zero"
