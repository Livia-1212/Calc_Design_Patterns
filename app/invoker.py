import pytest
from app.calculator import Command
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand



# Invoker Class for Interactive Mode
class Invoker:
    def __init__(self, calculator):
        self.calculator = calculator
        self.history = []

        # Command Dictionary
        self.command_menu = {
            "add <value>": "Add the specified value to the current result",
            "subtract <value>": "Subtract the specified value from the current result",
            "multiply <value>": "Multiply the current result by the specified value",
            "divide <value>": "Divide the current result by the specified value",
            "reset": "Reset the calculator to zero",
            "menu": "Display this menu of commands",
            "exit": "Exit the calculator program",
        }

    def execute_command(self, command: Command):
        """Execute a given command and add to history."""
        self.history.append(command)
        return command.execute()

    def show_menu(self):
        """Display the available commands and their descriptions."""
        print("\n **Available Commands**:")
        for command, description in self.command_menu.items():
            print(f"  - `{command}`: {description}")

    def start_repl(self):
        """Run the interactive REPL loop."""
        # Display the menu at the start
        self.show_menu()
        print("\nInteractive Calculator (REPL) with Command Pattern")
        print("Type 'menu' to see the available commands again.")

        while True:
            try:
                # Read User Input
                user_input = input("\n>>> ").strip().lower()

                # Exit Command
                if user_input == "exit":
                    print("Exiting Calculator... 🛑")
                    break

                # Show Menu Command
                if user_input == "menu":
                    self.show_menu()
                    continue

                # Reset Command
                if user_input == "reset":
                    self.calculator.value = 0
                    print(" Calculator reset. Current value is 0.")
                    continue

                # Parse Input into Command and Value
                parts = user_input.split()
                if len(parts) != 2:
                    print("Invalid input format. Use: command <value>")
                    continue

                command, value_str = parts
                try:
                    value = float(value_str)
                except ValueError:
                    print("Invalid value. Please enter a numeric value.")
                    continue

                # Execute Commands Based on Input
                if command == "add":
                    result = self.execute_command(AddCommand(self.calculator, value))
                elif command == "subtract":
                    result = self.execute_command(SubtractCommand(self.calculator, value))
                elif command == "multiply":
                    result = self.execute_command(MultiplyCommand(self.calculator, value))
                elif command == "divide":
                    result = self.execute_command(DivideCommand(self.calculator, value))
                else:
                    print("Unknown command. Type 'menu' to see available commands.")
                    continue

                # Print Result
                print(f"Result: {result}")

            except Exception as e:
                print(f"Error: {e}")
