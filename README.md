[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Run Tests](https://github.com/RakocevicN/Rick_n_Morty-Final-Project/actions/workflows/run-tests-all.yaml/badge.svg?branch=main)](https://github.com/RakocevicN/Rick_n_Morty-Final-Project/actions/workflows/run-tests-all.yaml)

# [Rick and Morty](https://rickandmortyapi.com/documentation)

This project uses Python 3.9.18 at the moment, because of the compatibility with Allure 2.16.0
* [Python 3.9.18](https://www.python.org/downloads/release/python-3918/)
* [Allure pytest documentation](https://allurereport.org/docs/pytest/)



## To start 

1. Clone the repository to your local machine and change into the project directory:
   * git clone https://github.com/RakocevicN/Rick_n_Morty-Final-Project.git 

2. Create virtual environment
   * python3.9 -m venv myenv 
  
3. Activate virtual environment:
   * source myenv/bin/activate

4. Install requirementas:
   * pip install -r requirements.txt

5. Download and install Allure
   * wget https://github.com/allure-framework/allure2/releases/download/2.16.0/allure-2.16.0.tgz

6. Extracted the package and moved it to the /opt directory
   * tar -xzvf allure-2.16.0.tgz
   * sudo mv allure-2.16.0 /opt/allure-2.16.0
7. Create symbolic link in the bin directory to make Allure cmd-line globally accessible
   * sudo ln -s /opt/allure-2.16.0/bin/allure /usr/bin/allure

## Project Structure

The project is organized into several components:

- `api_file`: Contains the main APIs for retrieving information about episodes, character IDs, and locations.
- `asserts`: Contains assertion functions for verifying the correctness of API responses for each test.
- `test_data`: Contains test data dictionaries used in test cases for each test.
- `tests`: Contains test files for episodes, id's and locations, more about: [test/README.md](tests/README.md) 
- `config.py`: Configuration file for project settings.
- `test_execution.py`: Script for running tests concurrently and to generate Allure report once tests are finished, more about: [test/README.md](tests/README.md)



