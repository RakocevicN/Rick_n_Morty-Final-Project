

## Overview of Tests
This project includes a  set of tests to ensure the functionality and reliability of [Rick and Morty](https://rickandmortyapi.com/documentation). The tests are organized into three main categories, each targeting a specific aspect of the API:
### Episode Tests

- Located in `tests/test_episode.py`.
- Tests the retrieval of episode information based on episode IDs.
- Verifies that the API responses match the expected data.

### ID Tests

- Located in `tests/test_id.py`.
- Contains positive and negative tests for character IDs.
- Verifies character information retrieval based on character IDs.
- Handles both positive scenarios with valid character IDs and negative scenarios with invalid character IDs.

### Location Tests

- Located in `tests/test_location.py`.
- Tests the retrieval of location information based on location names.
- Verifies that the API responses match the expected data.

---
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

---
# Testing with GitHub Actions

This project have GH Actions to automaticly run tests after each PR. Additionally, you can manually trigger test workflows using GitHub Actions.

---

## Running Tests 

When you create a new PR, GitHub Actions will automatically initiate a test workflow. The workflow will execute a set of tests to verify the that everything is as expected. You can review the test results in the PR's checks or statuses.

---
## Running Tests Manually

You also have the option to manually trigger test workflows using GitHub Actions. This allows to choose specific tests that needed for run:

-  Go to the Actions tab of this repository.
-  You will find a list of available workflows. 
-  Click on the Run Tests workflow to view its details.
-  Click the Run workflow button on the top right corner of the workflow details page
-  Chose test that you want to run
-  Select green Runn Workflow button
---
## Monitoring Test Results

You can monitor the progress and results of test workflows in the Actions tab. Detailed information about test execution and any issues/failures will be available in the workflow logs.

---
[docs]: https://allurereport.org/docs/?source=github_allure2 "Allure documentation"

[license]: http://www.apache.org/licenses/LICENSE-2.0 "Apache License 2.0"
[site]: https://allurereport.org/?source=github_allure2 "Official Website"
[docs]: https://allurereport.org/docs/?source=github_allure2 "Documentation"

# Allure Report

This project is using Allure to provide detail test reports after each tests run. 




<img src="https://allurereport.org/public/img/allure-report.svg" height="85px" alt="Allure Report logo" align="right" />

- Learn more about Allure Report at [https://allurereport.org](https://allurereport.org)
- 📚 [Documentation](https://allurereport.org/docs/) – discover official documentation for Allure Report
- ❓ [Questions and Support](https://github.com/orgs/allure-framework/discussions/categories/questions-support) – get help from the team and community


---