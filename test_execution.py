import click
import subprocess
import os
from concurrent.futures import ThreadPoolExecutor
from config import report_root


@click.command()
@click.option('--test_episode', is_flag=True, help='To run episode tests. Use --test_episode')
@click.option('--test_id', is_flag=True, help='To run ID tests. Use --test_id')
@click.option('--test_location', is_flag=True, help='To run location tests. Use --test_location')
@click.option('--all_tests', is_flag=True, help='To run all tests. Use --all_tests')
@click.option('--allure_output',
              prompt='Specify the folder name for Allure test results['
                     '/root/Rick_n_Morty-Final-Project/allure_reports/tmp]')
def run_tests(test_episode, test_id, test_location, all_tests, allure_output):
    test_types = []

    if all_tests:
        test_types = ['episode', 'id', 'location']
        max_workers = 12
    else:
        max_workers = 6
        if test_episode:
            test_types.append('episode')
        if test_id:
            test_types.append('id')
        if test_location:
            test_types.append('location')

    if not test_types:
        click.echo("No test option specified. Please see --test_episode, --test_id, --test_location, or --all_tests")
    else:
        # Define the folder where Allure results will be saved
        allure_results_dir = os.path.join(report_root, allure_output)

        # If allure_results directory doesn't exist it create
        if not os.path.exists(allure_results_dir):
            os.makedirs(allure_results_dir)

        os.environ["ALLURE_REPORT_ENVIRONMENT"] = "true"

        execute_tests_concurrently(test_types, max_workers, allure_results_dir)

        # Generate the Allure report
        generate_allure_report(allure_results_dir)


def execute_tests(test_type=None, allure_results_dir=None):
    subprocess.run(
        ["pytest", "tests" if test_type is None else f"tests/test_{test_type}.py", f"--alluredir={allure_results_dir}"],
        check=True
    )


def execute_tests_concurrently(test_types, max_workers, allure_results_dir):
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        ex.map(execute_tests, test_types, [allure_results_dir] * len(test_types))


def generate_allure_report(allure_results_dir):
    subprocess.run(["allure", "generate", allure_results_dir, "-o", "allure_report", "--clean"])


if __name__ == '__main__':
    run_tests()
