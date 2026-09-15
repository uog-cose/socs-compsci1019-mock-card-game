# Introduction

Mocking allows you to test your application completely. It allows you to mock user input and input from files and databases. The main libraries used is MagicMock, patch and mock_open. For this task you are required to implement several unit tests using these libraries.

# Instructions

- Fork this project and make sure your repository is public. Then import the project into your IDE (e.g., VSCode, PyCharm).
- You cannot change the signature of the provided functions or rename them.
- You cannot interact with your peers: work individually and do your best.
- The features to implement are described through a set of sub-tasks.
- Implement the functions one at a time, strictly following the order given by the sub-tasks. Do not read ahead to the following sub-tasks.
- A sub-task can be considered complete once you are confident that the required feature has been implemented correctly.
- Every time you complete a sub-task, commit and push your code.
- At the end of the assignment, make sure you have pushed the entire project to the repository.

# Sub-tasks

Remember to read and implement the sub-tasks one at a time, following the given order. Do not move on to the next sub-task until the current one has been completed. Implement the required features by working in the `task.py` file.

## Sub-task 1 – Mock Console Input

Mocking an input from the console.

### Requirement

* Open test/test_mock_ConsoleInOut.py
* See example unit test "test_get_input_string"
* Implement unit test "test_get_input_integer"
* Patch "card_game.communication.ConsoleInOut.get_string"
* Set return_value to be "3"
* Assert equal expected 3 to the result from get_input_integer("What is your age")

### Examples
* See example unit test "test_get_input_string"

## Sub-task 2 – Mock Console Game Info

Mocking an input from the console.

### Requirement

* Open test/test_mock_Game.py
* Implement unit test "test_get_game_info"
* Patch "card_game.communication.ConsoleInOut.get_string"
* Set side_effect to be a list "Derek" and 3
* Call get_game_info returning name and number_of_players
* Assert equal expected 3 to number_of_players

### Examples
* See example unit test "test_get_input_string"

## Sub-task 3 – Mock Console Input With Built In

Mocking an input from the console.

### Requirement

* Open test/test_mock_ConsoleInOut.py
* Implement unit test "test_get_input_string_builtin"
* Patch "builtins.input"
* Set return value equal "Derek"
* Assert equal expected "Derek" to equal get_input_string("What is your name")

### Examples
* See example unit test "test_get_input_string"

## Sub-task 4 – Mock File Load

Mocking an input from the console.

### Requirement

* Open test/test_mock_LoadCSV.py
* Implement unit test "test_get_csv_rows"
* Patch "builtins.open" and pass mock_open(read_data="Derek\nXi")
* Assert equal expected "Xi" to equal get_csv_rows("test.txt")[1][0]

### Examples
* See example unit test "test_get_input_string"

## Sub-task 5 – Mock Get Player Names

Mocking an input from the console.

### Requirement

* Open test/test_mock_Game.py
* Implement unit test "test_get_computer_players_names"
* Patch "builtins.open" and pass mock_open(read_data="DEALER,Derek\nCOMPUTER,Xi")
* Assert equal expected "Xi" to equal get_computer_players_names()[1]

### Examples
* See example unit test "test_get_input_string"

# Run Tests

python -m unittest discover -v -s ./test/ -p test_*.py