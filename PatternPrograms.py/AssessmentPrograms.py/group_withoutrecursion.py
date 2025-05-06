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

@cli.group()
def password():
    """Password-related operations"""
    pass

@password.command("validate")
@click.option('--password', prompt="Enter a secure password", type=str)
def validate_password(password):
    try:
        app.check_valid_password(password)
        click.echo("Password is valid.")
    except ValueError as e:
        click.echo(f"{e}")

@cli.group()
def number():
    """Number-related operations"""
    pass

@number.command("second-largest")
@click.option('--numbers', prompt="Enter numbers", type=int, nargs=-1)
def second_largest(numbers):
    try:
        result = app.second_largest(list(numbers))
        click.echo(f"Second Largest: {result}")
    except Exception as e:
        click.echo(f"{e}")

@number.command("target-sum")
@click.option('--numbers', prompt="Enter numbers", type=int, nargs=-1)
@click.option('--target', prompt="Enter target sum", type=int)
def target_sum(numbers, target):
    try:
        result = app.find_target_sum_indices(list(numbers), target)
        click.echo(f"Target sum indices: {result}")
    except Exception as e:
        click.echo(f"{e}")

@cli.group()
def string():
    """String-related operations"""
    pass

@string.command("count-chars")
@click.option('--chars', prompt="Enter characters", type=str, nargs=-1)
def count_chars(chars):
    try:
        result = app.count_contiguous_characters(list(chars))
        click.echo(f"Character counts: {result}")
    except Exception as e:
        click.echo(f"{e}")

@string.command("palindrome")
@click.option('--value', prompt="Enter string to check", type=str)
def check_palindrome(value):
    result = app.is_palindrome(value)
    click.echo("It is a palindrome." if result else "Not a palindrome.")

@cli.command()
@click.option('--num', prompt="Enter a number", type=int)
def reverse_triangle(n):
    app.print_reverse_triangle(n)

@string.command("swap-case")
@click.option('--text', prompt="Enter text", type=str)
def swap_case(text):
    result = app.swap_case(text)
    click.echo(f"Swapped case: {result}")

if __name__ == '__main__':
    cli()
