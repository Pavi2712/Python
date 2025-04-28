import click
import re

class AssessmentProgram:
    
    def check_valid_password(self, password_val: str) -> tuple[bool, list[str]]:
        """
        Validates the password based on several rules.
        """
        try:
            if len(password_val) < 8:
                raise ValueError("Password must be at least 8 characters long.")
            if not re.search(r'[A-Z]', password_val):
                raise ValueError("Password must contain at least one capital letter.")
            if not re.search(r'[a-z]', password_val):
                raise ValueError("Password must contain at least one lowercase letter.")
            if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password_val):
                raise ValueError("Password must contain at least one special character.")
            return True, None
        except ValueError as e:
            return False, [str(e)]        

    def second_largest(self, numbers: list[int]) -> int:
        """
        Returns the second largest number in the list.
        """
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required to find the second largest.")
        unique_numbers = list(set(numbers))
        unique_numbers.sort(reverse=True)
        return unique_numbers[1]

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
        """
        Counts contiguous characters in the list and returns a list of formatted results.
        """
        freq = {}
        for char in char_list:
            if char:
                freq[char] = freq.get(char, 0) + 1
        return [str(count) + char for char, count in freq.items()]

    def is_palindrome(self, value: str) -> bool:
        """
        Checks if the given string or number is a palindrome.
        """
        original = str(value)
        reversed_str = original[::-1]
        return original == reversed_str

    def print_reverse_triangle(self, n: int) -> None:
        """
        Prints a reverse triangle pattern of numbers.
        """
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                print(j, end=' ')
            print()

    def swap_case(self, inp: str) -> str:
        """
        Swaps cases of all characters in a string.
        """
        return inp.swapcase()

    def display_menu(self) -> None:
        """
        Displays the menu of available options.
        """
        click.echo("""Choose a program:
0: Password Validator
1: Find Second Largest Number
2: Print Reverse Triangle
3: Swap Case in String
4: Count Contiguous Characters
5: Find Indices Matching Target
6: Check for Palindrome
7: Exit
""")

    def run(self) -> None:
        """
        Runs the interactive CLI program using click.
        """
        while True:
            self.display_menu()

            try:
                choice_input = click.prompt("Enter your choice (0-7)", type=str)
                if choice_input == '7' or choice_input.lower() == 'exit':
                    click.echo("Exiting program.")
                    break

                choice = int(choice_input)

                match choice:
                    case 0:
                        string_val = click.prompt("Enter password", type=str)
                        valid, errors = self.check_valid_password(string_val)
                        if valid:
                            click.echo("Password is valid.")
                        else:
                            click.echo("Password did not match the criteria:")
                            for error in errors:
                                click.echo(f" - {error}")

                    case 1:
                        user_input = click.prompt("Enter list of numbers separated by space", type=str)
                        numbers = list(map(int, user_input.strip().split()))
                        result = self.second_largest(numbers)
                        click.echo(f"Second Largest: {result}")

                    case 2:
                        n = click.prompt("Enter value of n", type=int)
                        self.print_reverse_triangle(n)

                    case 3:
                        inp = click.prompt("Enter a string to swap case", type=str)
                        click.echo("Swapped String: " + self.swap_case(inp))

                    case 4:
                        user_input = click.prompt("Enter characters separated by space:", type=str)
                        chars = user_input.strip().split()
                        click.echo(f"Result: {self.count_contiguous_characters(chars)}")

                    case 5:
                        user_input = click.prompt("Enter list of numbers separated by space:", type=str)
                        numbers = list(map(int, user_input.strip().split()))
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

            except ValueError:
                click.echo("Please enter a valid integer choice.")

            cont = click.confirm("\nDo you want to continue?", default= True)
            if not cont:
                click.echo("Thank you! Exiting now.")
                break

@click.command()    
def main() -> None:
    """
    Runs the assessment program with a menu using the click package.
    """
    app = AssessmentProgram()
    app.run()

if __name__ == '__main__':
    main()
