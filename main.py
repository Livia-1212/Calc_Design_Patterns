from app.calculator import Calculator
from app.invoker import Invoker

def interactive_calculator():
    # Initialize calculator and invoker
    calculator = Calculator()
    invoker = Invoker(calculator)

    # Display the menu at the start
    invoker.show_menu()

# Main Function to Run the Interactive Calculator
if __name__ == "__main__":
    calculator = Calculator()
    invoker = Invoker(calculator)
    invoker.start_repl()
