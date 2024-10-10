# Calc_Design_Patterns

## Calculator includes function: add, subtract, multiply, divide

### Project Structure
cal_design_patterns 
##
>app/ 
>>    __init__.py         &nbsp; &nbsp; Package-level initialization code \
>>   calculator.py        &nbsp; &nbsp; Core calculator logic (Receiver) \
>>   command_handler.py   &nbsp; &nbsp; CommandHandler class to manage command registration and execution \
>>   commands.py          &nbsp; &nbsp; Command classes (Add, Subtract, Multiply, Divide) \
>>    invoker.py          &nbsp; &nbsp; Invoker class to manage command execution and REPL interface  \
>>    plugin_loader.py    &nbsp; &nbsp; Dynamically loads all command plugins from the specified plugins package
##
>plugins/
>> __init__.py            &nbsp; &nbsp;  Marks the 'plugins' directory as a package \
>> arithmetic/              &nbsp; &nbsp; Subfolder for arithmetic commands \
>>> __init__.py          &nbsp; &nbsp; Contains AddCommand, SubtractCommand, MultiplyCommand, and DivideCommand \
>> reset/                 &nbsp; &nbsp; Subfolder for reset-related commands \
>>> __init__.py          &nbsp; &nbsp; Contains ResetCommand implementation \
>> square/               &nbsp; &nbsp; Subfolder square commands \
>>> __init__.py          &nbsp; &nbsp; Contains square

## 
>tests/ 
>>   __init__.py           &nbsp; &nbsp; Indicates that 'tests' is a  package (optional) \
>>    conftest.py          &nbsp; &nbsp; Test fixtures shared across multiple test files \
>>    test_calculator.py   &nbsp; &nbsp; Unit tests for Calculator class \
>>    test_commands.py     &nbsp; &nbsp; Unit tests for Command classes \
>>    test_invoker.py      &nbsp; &nbsp; Unit tests for the Invoker and REPL interface 
##
> README.md                 &nbsp; &nbsp; Project documentation \
> main.py                 &nbsp; &nbsp; Entry point for the application 

##
### Project Details
Language: Python \
Design Pattern Used: Command Pattern \
Purpose: Demonstrate a modular, pattern-based design using a simple calculator.

