import click
import subprocess

"""
Run different sets of tests:
    --test_episode/--test_id/--test_location/--all_tests (bool):
    Set these flags to True to execute the corresponding tests, or False to skip them.
@click.command() decorator is used to define CLI commands.
@click.option() decorators are used to define command-line options.  
For more about click, please visit: https://click.palletsprojects.com/en/8.1.x/
"""


@click.command()
@click.option('--test_episode', is_flag=True, help='Run episode tests. Use --test_episode')
@click.option('--test_id', is_flag=True, help='Run ID tests. Use --test_id')
@click.option('--test_location', is_flag=True, help='Run location tests. Use --test_location')
@click.option('--all_tests', is_flag=True, help='To run all tests. Use --all_tests')
def run_tests(test_episode, test_id, test_location, all_tests):
    if all_tests:
        run_all_tests()
    elif test_episode:
        run_specific_tests('episode')
    elif test_id:
        run_specific_tests('id')
    elif test_location:
        run_specific_tests('location')
    else:
        click.echo("No test option specified. Please see --test_episode, --test_id, --test_location, or --all.")


def run_all_tests():
    try:
        subprocess.run(["pytest", "tests"])
    except Exception as problem:
        print(f"Problem while running all tests: {problem}")


def run_specific_tests(test_type):
    try:
        subprocess.run(["pytest", f"tests/test_{test_type}.py"])
    except Exception as problem:
        print(f"Problem while running {test_type} test: {problem}")


if __name__ == '__main__':
    run_tests()
