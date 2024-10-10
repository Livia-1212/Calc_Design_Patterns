# Invoker to implement REPL behavnior and command pattern interactive interface

class Invoker:
    def __init__(self, command_handler):
        """Initialize the Invoker with the provided command handler."""
        self.command_handler = command_handler
        self.history = []

        # Command Dictionary (Menu) - Maps command names to descriptions
        self.command_menu = {
            "add <value>": "Add the specified value to the current result",
            "subtract <value>": "Subtract the specified value from the current result",
            "multiply <value>": "Multiply the current result by the specified value",
            "divide <value>": "Divide the current result by the specified value",
            "exponent <base> <exponent>": "Calculate base raised to the power of exponent",
            "square <value>": "Calculate the square of the specified value",
            "reset": "Reset the calculator to zero",
            "menu": "Display this menu of commands",
            "exit": "Exit the calculator program",
        }

    def show_menu(self):
        """Display the available commands and their descriptions."""
        print("\n📜 **Available Commands**:")
        for command, description in self.command_menu.items():
            print(f"  - `{command}`: {description}")

    def execute_command(self, command_name: str):
        command = self.command_handler.commands.get(command_name)
        if command is None:
            print(f"Error: Command '{command_name}' not found.")
            return None

        # Execute the command if found and add to history
        self.history.append(command)
        return command.execute()

    def start_repl(self):
        """Interactive REPL loop for the calculator using CommandHandler."""
        print("\nWelcome to the Interactive Calculator (CommandHandler Pattern) 💻")
        self.show_menu()  # Show the menu at the start

        while True:
            user_input = input("\n>>> ").strip().lower()
            
            if user_input == "exit":
                print("Exiting calculator... 🛑")
                break

            if user_input == "menu":
                self.show_menu()
                continue

            if user_input == "reset":
                result = self.execute_command("reset")
                print(f"Calculator reset. Current value is {result}.")
                continue

            # Parse user input into command and value(s)
            parts = user_input.split()
            if len(parts) < 1:
                print("Invalid format. Use: command <value(s)>")
                continue

            command_name = parts[0]
            values = parts[1:]

            # Handle specific commands that require multiple values (e.g., exponent)
            if command_name == "exponent":
                if len(values) != 2:
                    print("Invalid format for `exponent`. Use: exponent <base> <exponent>")
                    continue

                # Set up the exponent command values
                try:
                    base, exponent_value = map(float, values)
                except ValueError:
                    print("Invalid values. Please enter numeric values for base and exponent.")
                    continue

                # Register the command and update its values
                command = self.command_handler.commands.get("exponent")
                if command:
                    command.base = base
                    command.exponent = exponent_value
                else:
                    print(f"Error: Command '{command_name}' is not registered.")
                    continue

            # Handle commands that require a single value (e.g., add, subtract, square)
            elif command_name in ["add", "subtract", "multiply", "divide", "square"]:
                if len(values) != 1:
                    print(f"Invalid format for `{command_name}`. Use: {command_name} <value>")
                    continue

                # Get the value as a float
                try:
                    value = float(values[0])
                except ValueError:
                    print("Invalid value. Please enter a numeric value.")
                    continue

                # Register the command with the parsed value
                command = self.command_handler.commands.get(command_name)
                if command:
                    command.value = value  # Update the command value dynamically
                else:
                    print(f"Error: Command '{command_name}' is not registered.")
                    continue

            # Execute the command using its name
            result = self.execute_command(command_name)
            if result is not None:
                print(f"🧮 Result: {result}")
