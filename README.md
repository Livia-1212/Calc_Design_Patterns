# Calc_Design_Patterns

## Calculator includes function: add, subtract, multiply, divide

### Project Structure
cal_design_patterns
── app/__
|    __init__.py           # Package-level initialization code \
│    calculator.py         # Core calculator logic (Receiver) \
│    commands.py           # Command classes (Add, Subtract, Multiply, Divide) \
│    invoker.py            # Invoker class to manage command execution and REPL interface \ ──tests/ __
|    __init__.py           # Indicates that 'tests' is a  package (optional) \
│    conftest.py           # Test fixtures shared across multiple test files \
│    test_calculator.py    # Unit tests for Calculator class \
│    test_commands.py      # Unit tests for Command classes \
│    test_invoker.py       # Unit tests for the Invoker and REPL interface \
 README.md                 # Project documentation \
 main.py                 # Entry point for the application \


### Project Details
Language: Python
Design Pattern Used: Command Pattern
Purpose: Demonstrate a modular, pattern-based design using a simple calculator.

