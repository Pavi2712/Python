import click
import re

class AssessmentProgram:
    
    def check_valid_password(self, password_val: str) -> None:
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$' #.* any characters (zero or more) , (?=.*[a-z]) -> Atleast one small lowercase
        if not re.match(pattern, password_val):
            raise ValueError("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (@#$%^&+=!).")

    def second_largest(self, numbers: list[int]) -> int:
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required to find the second largest.")
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[j] > numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers[1]

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
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
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

    def display_menu(self) -> None:
        click.echo("""\nChoose a program:
        0: Password Validator
        1: Find Second Largest Number
        2: Print Reverse Triangle
        3: Swap Case in String
        4: Count Contiguous Characters
        5: Find Indices Matching Target
        6: Check for Palindrome
        7: Exit
        """)

    def run(self, choice: int = None) -> None:
        try:
            if choice is None:
                self.display_menu()
                choice = click.prompt("Enter your choice (0-7)", type=int)
            match choice:
                case 0:
                    try:
                        string_val = click.prompt("Enter password", type=str)
                        self.check_valid_password(string_val)
                    except ValueError as e:
                        click.echo(e)
                    else:
                        click.echo("Password matched the criteria")
                case 1:
                    nums = click.prompt("Enter list of numbers separated by space", type=str)
                    numbers = list(map(int, nums.split()))
                    result = self.second_largest(numbers)
                    click.echo(f"Second Largest: {result}")
                case 2:
                    n = click.prompt("Enter value of n", type=int)
                    self.print_reverse_triangle(n)
                case 3:
                    inp = click.prompt("Enter a string to swap case", type=str)
                    result = self.swap_case(inp)
                    click.echo(f"Swapped String: {result}")
                case 4:
                    chars = click.prompt("Enter characters separated by space:", type=str)
                    char_list = chars.split()
                    click.echo(f"Result: {self.count_contiguous_characters(char_list)}")
                case 5:
                    nums = click.prompt("Enter list of numbers separated by space:", type=str)
                    numbers = list(map(int, nums.split()))
                    target_val = click.prompt("Enter target value", type=int)
                    click.echo(f"Result: {self.find_target_sum_indices(numbers, target_val)}")
                case 6:
                    val = click.prompt("Enter a string or number", type=str)
                    if self.is_palindrome(val):
                        click.echo("It is a palindrome.")
                    else:
                        click.echo("It is not a palindrome.") 
                case _:
                    click.echo("Invalid choice. Please enter a number from 0 to 7.")
        except Exception as e:
            click.echo(f"Error: {e}")

        cont = click.confirm("\nDo you want to continue?", default=True)
        if cont:
            self.display_menu()
            choice_input = click.prompt("Enter your choice (0-7)", type=int)
            self.run(choice_input)

@click.command(context_settings=dict(default_map={'choice': 0}))
@click.option('--choice', type=int, help="Program choice to run")
def main(choice):
    """
    Runs the assessment program with menu options.
    """
    app = AssessmentProgram()
    app.run(choice)

if __name__ == '__main__':
    main()
