import click
import re

class AssessmentProgram:
    def check_valid_password(self, password_val: str) -> None:
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
        if not re.match(pattern, password_val):
            raise ValueError(
                "Password must be at least 8 characters long and include at least one uppercase letter, "
                "one lowercase letter, one number, and one special character (@#$%^&+=!)."
            )

    def second_largest(self, numbers: list[int]) -> int:
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required to find the second largest.")
        sorted_nums = sorted(set(numbers), reverse=True)
        return sorted_nums[1]

    def find_target_sum_indices(self, numbers: list[int], target: int) -> list[list[int]]:
        result = []
        for start in range(len(numbers)):
            total = numbers[start]
            indices = [start]
            for end in range(start + 1, len(numbers)):
                total += numbers[end]
                indices.append(end)
                if total == target:
                    result.append(indices)
                    break
                elif total > target:
                    break
        return result

    def count_contiguous_characters(self, char_list: list[str]) -> list[str]:
        freq = {}
        for char in char_list:
            if char:
                freq[char] = freq.get(char, 0) + 1
        return [str(count) + char for char, count in freq.items()]

    def is_palindrome(self, value: str) -> bool:
        original = str(value)
        reversed_str = ''
        for index in range(len(original) - 1, -1, -1):
            reversed_str += original[index]
        return original == reversed_str

    def print_reverse_triangle(self, n: int) -> None:
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                print(j, end=' ')
            print()

    def swap_case(self, inp: str) -> str:
        result = ""
        for char in inp:
            if char.isupper():
                result += char.lower()
            elif char.islower():
                result += char.upper()
            else:
                result += char
        return result


app = AssessmentProgram()


@click.group()
def cli():
    """Assessment Program CLI"""
    pass

#Function 

@cli.command()
@click.option('--password', prompt="Enter a secure password", type=str)
def validate_password(password):
    try:
        app.check_valid_password(password)
        click.echo("Password is valid.")
    except ValueError as e:
        click.echo(f"{e}")
    prompt_continue("validate_password")


@cli.command()
@click.option('--numbers', prompt="Enter numbers separated by space", type=str)
def second_largest(numbers):
    try:
        num_list = list(map(int, numbers.split()))
        result = app.second_largest(num_list)
        click.echo(f"Second Largest: {result}")
    except Exception as e:
        click.echo(f"{e}")
    prompt_continue("second_largest")


@cli.command()
@click.option('--numbers', prompt="Enter numbers separated by space", type=str)
@click.option('--target', prompt="Enter target sum", type=int)
def target_sum(numbers, target):
    try:
        num_list = list(map(int, numbers.split()))
        result = app.find_target_sum_indices(num_list, target)
        click.echo(f"Target sum indices: {result}")
    except Exception as e:
        click.echo(f"{e}")
    prompt_continue("target_sum")


@cli.command()
@click.option('--chars', prompt="Enter characters separated by space", type=str)
def count_chars(chars):
    try:
        char_list = chars.split()
        result = app.count_contiguous_characters(char_list)
        click.echo(f"Character counts: {result}")
    except Exception as e:
        click.echo(f"{e}")
    prompt_continue("count_chars")


@cli.command()
@click.option('--value', prompt="Enter string to check", type=str)
def check_palindrome(value):
    result = app.is_palindrome(value)
    click.echo("It is a palindrome." if result else "Not a palindrome.")
    prompt_continue("check_palindrome")


@cli.command()
@click.option('--n', prompt="Enter a number", type=int)
def reverse_triangle(n):
    app.print_reverse_triangle(n)
    prompt_continue("reverse_triangle")


@cli.command()
@click.option('--text', prompt="Enter text", type=str)
def swap_case(text):
    result = app.swap_case(text)
    click.echo(f"Swapped case: {result}")
    prompt_continue("swap_case")

# Infinite handling

def prompt_continue(current_command):
    if click.confirm("Do you want to continue with the same case?", default=True):
        _reinvoke(current_command)
    elif click.confirm("Do you want to continue with other cases?", default=True):
        _choose_and_invoke()
    else:
        click.echo("Exiting!")


def _reinvoke(command_name: str):
    click.echo(f"\nRe-running {command_name}...\n")
    globals()[command_name]()  # Calls the function 


def _choose_and_invoke():
    options = [
        "validate_password",
        "second_largest",
        "target_sum",
        "count_chars",
        "check_palindrome",
        "reverse_triangle",
        "swap_case"
    ]
    click.echo("\nAvailable cases:")
    for opt in options:
        click.echo(f" - {opt}")
    selected = click.prompt("\nEnter the name of the case you want to run", type=click.Choice(options))
    _reinvoke(selected)

if __name__ == '__main__':
    cli()
