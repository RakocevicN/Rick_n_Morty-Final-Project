import click
import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

DEFAULT_ALLURE_PORT = 46869
localhost = '172.31.58.199'
# Define the report_root path
report_root = "/root/Rick_n_Morty-Final-Project/allure_reports"


@click.command()
@click.option('--test_episode', is_flag=True, help='To run episode tests. Use --test_episode')
@click.option('--test_id', is_flag=True, help='To run ID tests. Use --test_id')
@click.option('--test_location', is_flag=True, help='To run location tests. Use --test_location')
@click.option('--all_tests', is_flag=True, help='To run all tests. Use --all_tests')
@click.option('--allure_output',
              prompt='Specify the folder name for Allure test results[/root/Rick_n_Morty-Final-Project/allure_reports/tmp]')
@click.option('--allure_port', default=DEFAULT_ALLURE_PORT, help='Specify the Allure server port')
@click.option('--allure_host', default='localhost', help='Specify the Allure server host')
def run_tests(test_episode, test_id, test_location, all_tests, allure_output, allure_port, allure_host):
    test_types = []

    if all_tests:
        test_types = ['episode', 'id', 'location']
        max_workers = 9
    else:
        max_workers = 5
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

        # Create the allure_results directory if it doesn't exist
        if not os.path.exists(allure_results_dir):
            os.makedirs(allure_results_dir)

        # Set the Allure environment properties using environment variables
        os.environ["ALLURE_REPORT_ENVIRONMENT"] = "true"

        # Execute tests and generate Allure results
        execute_tests_concurrently(test_types, max_workers, allure_results_dir, allure_port)

        # Generate the Allure report
        generate_allure_report(allure_results_dir, allure_port)

        # Print the URL to the generated report
        allure_url = f"http://:172.31.58.199{allure_port}/index.html#"
        click.echo(f"Allure report is available at: {allure_url}")


def execute_tests(test_type=None, allure_results_dir=None, allure_port=DEFAULT_ALLURE_PORT):
    # Pass the allure_results_dir and allure_port to subprocess.run
    subprocess.run(
        ["pytest", "tests" if test_type is None else f"tests/test_{test_type}.py", f"--alluredir={allure_results_dir}"],
        check=True
    )


def execute_tests_concurrently(test_types, max_workers, allure_results_dir, allure_port):
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        # Pass allure_results_dir and allure_port to the execute_tests function
        ex.map(execute_tests, test_types, [allure_results_dir] * len(test_types), [allure_port] * len(test_types))


def generate_allure_report(allure_results_dir, allure_port):
    subprocess.run(["allure", "generate", allure_results_dir, "-o", "allure_report", "--clean"])
    # Start Allure server with the specified host and port
    subprocess.run(["allure", "serve", allure_results_dir, "--host", "localhost", "--port", str(allure_port)])


if __name__ == '__main__':
    run_tests()