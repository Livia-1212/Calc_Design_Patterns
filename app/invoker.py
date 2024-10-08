# app/invoker.py

from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class Invoker:
    def __init__(self, command_handler):
        self.command_handler = command_handler
        self.history = []

        # Command Dictionary (Menu)
        self.command_menu = {
            "add <value>": "Add the specified value to the current result",
            "subtract <value>": "Subtract the specified value from the current result",
            "multiply <value>": "Multiply the current result by the specified value",
            "divide <value>": "Divide the current result by the specified value",
            "reset": "Reset the calculator to zero",
            "menu": "Display this menu of commands",
            "exit": "Exit the calculator program",
        }

    def execute_command(self, command_name: str):
        """Retrieve and execute a command from the CommandHandler by its name."""
        # Retrieve the command from the CommandHandler's `commands` dictionary
        command = self.command_handler.commands.get(command_name)
        
        if command is None:
            print(f"Error: Command '{command_name}' not found.")
            return None

        # Execute the command if found
        self.history.append(command)
        return command.execute()

    def show_menu(self):
        """Display the available commands and their descriptions."""
        print("\n**Available Commands**:")
        for command, description in self.command_menu.items():
            print(f"  - `{command}`: {description}")

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
                self.show_menu()  # Display the menu again
                continue

            if user_input == "reset":
                result = self.command_handler.execute_command("reset")
                print(f"Calculator reset. Current value is {result}.")
                continue

            # Parse user input into command and value
            parts = user_input.split()
            if len(parts) != 2:
                print("Invalid format. Use: command <value>")
                continue

            command_name, value_str = parts
            try:
                value = float(value_str)
            except ValueError:
                print("Invalid value. Please enter a numeric value.")
                continue

            # registration of the command based input
            if command_name in ["add", "subtract", "multiply", "divide"]:
                # Get the registered command and update its value
                command = self.command_handler.commands.get(command_name)
                if command:
                    command.value = value
                else:
                    print(f"Error: Command '{command_name}' is not registered.")
                    continue
            else:
                print("Unknown command. Type `menu` to see the available commands.")
                continue

            # Execute the command using its name
            result = self.execute_command(command_name)
            print(f"Result: {result}")
