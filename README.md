# Introduction

Mocking allows you to test your application completely. It allows you to mock user input and input from files and databases. The main libraries used for this purpuse are `MagicMock`, `patch` and `mock_open`. For this task you are required to implement several unit tests using these libraries.

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

* Open test/test_mock_ConsoleInOut.py
* Implement unit test `test_get_input_string`
* We want to test `ConsoleInOut.get_input_string` that calls `get_string` to get an input from the console.
* Mock `get_string` to return "Derek"
* Assert equal expected Derek to the result from get_input_string("What is your name")
* Run test and check passes

### Example
* See example unit test "test_get_input_string" in test/test_mock_ConsoleInOut.py

## Sub-task 1 – Mock Console Input

To mock an input from the console.

### Requirement

* Open test/test_mock_ConsoleInOut.py
* Implement unit test "test_get_input_integer"
* We want to test `ConsoleInOut.get_input_integer` that calls `get_string` to get an input from the console.
* Mock `get_string` to return "18"
* Assert equal expected 18 to the result from get_input_integer("What is your age")
* Run test and check passes

### Example
* See example unit test "test_get_input_string"

## Sub-task 2 – Mock Console Game Info

To mock an input from the console.

### Requirement

* Open `test/test_mock_Game.py`
* Implement unit test `test_get_game_info`
* Get "ConsoleInOut.get_string" to return "Derek" and then 3
* We want to test `Game.get_game_info` that calls `get_input_string` and `get_input_integer` to get an inputs from the console.
* Mock `get_string` to return "Derek" and then "3"
* Assert equal expected 3 to number_of_players
* Run test and check passes

## Sub-task 3 – Mock Console Input With Built In

To mock an input from the console.

### Requirement

* Open `test/test_mock_ConsoleInOut.py`
* Implement unit test `test_get_input_string_builtin`
* We want to test `ConsoleInOut.get_input_string` that calls `get_string` that calls the built in `input` Python method.
* Mock built in `input` to return "Derek"
* Assert equal expected "Derek" to equal get_input_string("What is your name")
* Run test and check passes


## Sub-task 4 – Mock File Load

To mock an opening of a file.

### Requirement

* Open `test/test_mock_LoadCSV.py`
* Implement unit test `test_get_csv_rows`
* We want to test `LoadCSV.get_csv_rows` that calls `create_csv_reader` to open a file.
* Mock built in Python file open to return "Derek\nXi"
* Assert equal expected "Xi" to equal get_csv_rows("test.txt")[1][0]
* Run test and check passes

## Sub-task 5 – Mock Get Player Names

To mock an opening of a file.

### Requirement

* Open `test/test_mock_Game.py`
* Implement unit test `test_get_computer_players_names`
help_class
* We want to test `Game.get_computer_players_names` that calls `LoadCSV.get_csv_rows` that calls `create_csv_reader` to open a file.
* Mock built in Python file open to return "DEALER,Derek\nCOMPUTER,Xi"
* Assert equal expected "Xi" to equal get_computer_players_names()[1]
* Run test and check passes

# Run Tests

python -m unittest discover -v -s ./test/ -p test_*.py