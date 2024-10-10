#managing and executing commands independently using multiprocessing

from multiprocessing import Process, Manager

class Invoker:
    def __init__(self, command_handler):
        """Initialize the Invoker with the provided command handler."""
        self.command_handler = command_handler
        self.history = []  # Store executed commands

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
        print("\n📜 **Available Commands**:")
        for command, description in self.command_menu.items():
            print(f"  - `{command}`: {description}")

    def execute_command_in_process(self, command_name: str, calculator_state, process_result):
        """Run a command in a separate process."""
        command = self.command_handler.commands.get(command_name)
        if command is None:
            # Set the process result with the error message
            process_result.value = f"Error: Command '{command_name}' not found."
            return

        # Assign the shared state to the command's calculator attribute
        command.calculator.value = calculator_state.value

        # Execute the command and update the shared state
        try:
            result = command.execute()
        except ZeroDivisionError:
            result = "Error: Division by zero"

        calculator_state.value = command.calculator.value
        process_result.value = result

    def execute_command(self, command_name: str, calculator_state):
        """Execute a command in a separate process using multiprocessing."""
        process_result = Manager().Namespace()
        process_result.value = None

        # Create a separate process for command execution
        process = Process(target=self.execute_command_in_process, args=(command_name, calculator_state, process_result))
        process.start()
        process.join()  # Wait for the process to complete

        # Return the result of the command execution
        return process_result.value

    def start_repl(self):
        """Interactive REPL loop for the calculator using CommandHandler."""
        print("\nWelcome to the Interactive Calculator (Multiprocessing Mode) 💻")
        self.show_menu()  # Show the menu at the start

        # Create a manager for shared state
        with Manager() as manager:
            calculator_state = manager.Namespace()
            calculator_state.value = 0  # Initialize the shared state for calculator value

            while True:
                user_input = input("\n>>> ").strip().lower()

                if user_input == "exit":
                    print("Exiting calculator... 🛑")
                    break

                if user_input == "menu":
                    self.show_menu()
                    continue

                if user_input == "reset":
                    self.execute_command("reset", calculator_state)
                    print(f"Calculator reset. Current value is {calculator_state.value}.")
                    continue

                # Parse user input into command and value(s)
                parts = user_input.split()
                if len(parts) < 1:
                    print("Invalid format. Use: command <value(s)>")
                    continue

                command_name = parts[0]
                values = parts[1:]

                # Handle specific commands that require multiple values (e.g., exponent)
                if command_name in ["add", "subtract", "multiply", "divide", "square"]:
                    if len(values) != 1:
                        print(f"Invalid format for `{command_name}`. Use: {command_name} <value>")
                        continue

                    try:
                        value = float(values[0])
                    except ValueError:
                        print("Invalid value. Please enter a numeric value.")
                        continue

                    # Register the command and update its value
                    command = self.command_handler.commands.get(command_name)
                    if command:
                        command.value = value
                    else:
                        print(f"Error: Command '{command_name}' is not registered.")
                        continue

                # Execute the command using multiprocessing
                result = self.execute_command(command_name, calculator_state)
                
                # Print the result if it is an error message
                if isinstance(result, str) and "Error" in result:
                    print(result)
                else:
                    print(f"🧮 Result: {result} | Current Calculator Value: {calculator_state.value}")
