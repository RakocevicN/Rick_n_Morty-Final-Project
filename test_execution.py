import click
import subprocess
from concurrent.futures import ThreadPoolExecutor

"""
Run different sets of tests:
    --test_episode/--test_id/--test_location/--all_tests
    Set these flags to True to execute the corresponding tests
For more about click, please visit: https://click.palletsprojects.com/en/8.1.x/
"""


@click.command()
@click.option('--test_episode', is_flag=True, help='To run episode tests. Use --test_episode')
@click.option('--test_id', is_flag=True, help='To run ID tests. Use --test_id')
@click.option('--test_location', is_flag=True, help='To run location tests. Use --test_location')
@click.option('--all_tests', is_flag=True, help='To run all tests. Use --all_tests')
def run_tests(test_episode, test_id, test_location, all_tests):
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
        execute_tests_concurrently(test_types, max_workers)


def execute_tests(test_type=None):
    subprocess.run(["pytest", "tests" if test_type is None else f"tests/test_{test_type}.py"])


def execute_tests_concurrently(test_types, max_workers):
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        ex.map(execute_tests, test_types)


if __name__ == '__main__':
    run_tests()
