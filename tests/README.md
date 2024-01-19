# [Rick and Morty](https://rickandmortyapi.com/documentation)

This project uses Python 3.10.12 at the moment, more about Python 3.10.12 [here](https://www.python.org/downloads/release/python-31012/).

## Dependecines before executing tests

1. Clone the repository to your local machine and change into the project directory:
   * git clone https://github.com/RakocevicN/Rick_n_Morty-Final-Project.git 

2. Create virtual environment
   * python3 -m venv myenv
  
3. Activate virtual environment:
   * source myenv/bin/activate

4. Install requirementas:
   * install -r requirements.txt
  
## Overview of Tests
This project includes a  set of tests to ensure the functionality and reliability of [Rick and Morty](https://rickandmortyapi.com/documentation). The tests are organized into three main categories, each targeting a specific aspect of the API:
#### 1. Episode Tests
#### 2. Character ID Tests
#### 3. Location Tests


## Overview of `test_execution.py`

- `test_execution.py` is designed to execute different sets of tests.
- It allows you to specify which types of tests you want to run with various command-line options.
- The script uses multithreading to execute tests concurrently, and the level of parallelism can be configured based on the selected test options.

This script relies on the following Python modules:

- [Click](https://click.palletsprojects.com/en/8.1.x/) for CLI handling.
- `subprocess` for executing test commands
- `concurrent.futures.ThreadPoolExecutor` for multithreading

## Available options for `test_execution.py`
- `--test_episode`: To run episode tests
- `--test_id`: To run id tests
- `--test_location`: To run location tests
- `--all_tests`: To run all tests
## Accessing Help

To view the built-in help documentation for the `test_execution.py` script, you can use the following command:
python3 test_execution.py --help


# Testing with GitHub Actions

This project have GH Actions to automaticly run tests after each PR. Additionally, you can manually trigger test workflows using GitHub Actions.

## Running Tests 

When you create a new PR, GitHub Actions will automatically initiate a test workflow. The workflow will execute a set of tests to verify the that everything is as expected. You can review the test results in the PR's checks or statuses.

## Running Tests Manually

You also have the option to manually trigger test workflows using GitHub Actions. This allows to choose specific tests that needed for run:

-  Go to the Actions tab of this repository.
-  You will find a list of available workflows. 
-  Click on the Run Tests workflow to view its details.
-  Click the Run workflow button on the top right corner of the workflow details page
-  Chose test that you want to run
-  Select green Runn Workflow button

## Monitoring Test Results

You can monitor the progress and results of test workflows in the Actions tab. Detailed information about test execution and any issues/failures will be available in the workflow logs.

