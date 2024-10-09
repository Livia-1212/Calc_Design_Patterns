# Calculator for user to do basic operation add, subtract, multiply and divide
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, value):
        self.value += value
        return self.value

    def subtract(self, value):
        self.value -= value
        return self.value

    def multiply(self, value):
        self.value *= value
        return self.value

    def divide(self, value):
        if value == 0:
            return "Error: Division by zero"
        self.value /= value
        return self.value

    def reset(self):
        self.value = 0
        return self.value
