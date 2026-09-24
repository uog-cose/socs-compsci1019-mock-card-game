# Introduction

Mocking allows you to test your application completely. It allows you to mock user input from console, files and databases. The main libraries used from from `unittest.mock` are `patch` to mock console input and `mock_open` to mock opening files. For this task you are required to implement several unit tests using these libraries.

# Instructions

- Fork this project and make sure your repository is public. Then import the project into your IDE VSCode.
- You cannot change the signature of the provided functions or rename them.
- You cannot interact with your peers: work individually and do your best.
- The features to implement are described through a set of sub-tasks.
- Implement the functions one at a time, strictly following the order given by the sub-tasks. Do not read ahead to the following sub-tasks.
- A sub-task can be considered complete once you are confident that the required feature has been implemented correctly.
- Every time you complete a sub-task, commit and push your code.
- At the end of the assignment, make sure you have pushed the entire project to the repository.

# Sub-tasks

Remember to read and implement the sub-tasks one at a time, following the given order. Do not move on to the next sub-task until the current one has been completed. Implement the required features by working in the `test/test_mock_ConsoleInOut.py`, `test/test_mock_Game.py` & `test/test_mock_LoadCSV.py` files.

## Sub-task Example - Get Input String

To mock an input from the console.

### Requirement

* Implement unit test `test_get_input_string` in `test/test_mock_ConsoleInOut.py` to mock a method.
* This is a unit test for method `ConsoleInOut.get_input_string` that recieves a string input through `get_string` from the console.
* Mock the method `get_string` to return "Derek".
* The expected parameter in the unit test case is "Derek".
* The result parameter will call the method being tested and the test should pass.

### Example
* See example unit test "test_get_input_string" in test/test_mock_ConsoleInOut.py

## Sub-task 1 – Mock Console Input Integer

To mock an input from the console.

### Requirement

* Implement unit test `test_get_input_integer` in `test/test_mock_ConsoleInOut.py` to mock a method.
* We want to test `ConsoleInOut.get_input_integer` that calls `get_string` to get an input from the console.
* Mock the method `get_string` to return "18"
* The expected parameter in the unit test case is 18.
* The result parameter will call the method being tested and the test should pass.

### Example
* See example unit test "test_get_input_string"

## Sub-task 2 – Mock Console Game Info

To mock an input from the console.

### Requirement

* Implement unit test `test_get_game_info` in `test/test_mock_Game.py` to mock a method.
* Get "ConsoleInOut.get_string" to return "Derek" and then 3
* We want to test `Game.get_game_info` that calls `get_input_string` and `get_input_integer` to get an inputs from the console.
* Mock the method `get_string` to return "Derek" and then "3"
* The expected parameter in the unit test case is 3.
* The result parameter will call the method being tested and the test should pass.

## Sub-task 3 – Mock Console Input With Built In

To mock an input from the console.

### Requirement

* Implement unit test `test_get_input_string_builtin` in `test/test_mock_ConsoleInOut.py` to mock a built in python function.
* We want to test `ConsoleInOut.get_input_string` that calls `get_string` that calls the built in `input` Python method.
* Mock the built in `input` to return "Derek"
* The expected parameter in the unit test case is "Derek".
* The result parameter will call the method being tested and the test should pass.

## Sub-task 4 – Mock File Load

To mock an opening of a file.

### Requirement

* Implement unit test `test_get_csv_rows` in `test/test_mock_LoadCSV.py` to mock an opening.
* We want to test `LoadCSV.get_csv_rows` that calls `create_csv_reader` to open a file.
* Mock built in Python file open to return "Derek\nXi"
* The expected parameter in the unit test case is Xi.
* The result parameter will call the method being tested and the test should pass.

## Sub-task 5 – Mock Get Player Names

To mock an opening of a file.

### Requirement

* Implement unit test `test_get_computer_players_names` in `test/test_mock_Game.py` to mock an opening.
help_class
* We want to test `Game.get_computer_players_names` that calls `LoadCSV.get_csv_rows` that calls `create_csv_reader` to open a file.
* Mock built in Python file open to return "DEALER,Derek\nCOMPUTER,Xi"
* The expected parameter in the unit test case is Xi.
* The result parameter will call the method being tested and the test should pass.

# Run Tests

python -m unittest discover -v -s ./test/ -p test_*.py