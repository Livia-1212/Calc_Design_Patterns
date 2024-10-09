# tests/test_invoker.py
from app.commands import*

def test_invoker_execution(invoker, add_command):
    assert invoker.execute_command(add_command) == 10  # Should add 10
    assert invoker.calculator.value == 10  # Check calculator value

def test_invoker_history(invoker, add_command, subtract_command):
    invoker.execute_command(add_command)
    invoker.execute_command(subtract_command)
    assert len(invoker.history) == 2  # History should have two commands
    assert invoker.history[0] == add_command  # First command is add_command
    assert invoker.history[1] == subtract_command  # Second command is subtract_command

def test_show_menu(capsys, invoker):
    invoker.show_menu()
    captured = capsys.readouterr()
    assert "Available Commands" in captured.out  # Check that menu is displayed
