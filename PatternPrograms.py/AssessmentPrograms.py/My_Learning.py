from ast import literal_eval
import click
import re

class AssessmentProgram:
    def check_valid_password(self, password_val):
        """
        Validates the password based on several rules.
        """
        try:
            # Check for minimum length
            if len(password_val) < 8:
                raise ValueError("Password must be at least 8 characters long.")
            
            # Check for at least one uppercase letter
            if not re.search(r'[A-Z]', password_val):
                raise ValueError("Password must contain at least one capital letter.")
            
            # Check for at least one lowercase letter
            if not re.search(r'[a-z]', password_val):
                raise ValueError("Password must contain at least one lowercase letter.")
            
            # Check for at least one special character
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password_val):
                raise ValueError("Password must contain at least one special character.")
            
            return True
        except ValueError as e:
            return False, str(e)        
    
    def second_largest(self, numbers):
        """
        Returns the second largest number in the list.
        """
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required to find the second largest.")
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[j] > numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers[1]

    def find_target_sum_indices(self, numbers, target):
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

    def count_contiguous_characters(self, char_list):
        """
        Counts contiguous characters in the list and returns a list of formatted results.
        """
        freq = {}
        for char in char_list:
            if char:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
        return [str(count) + char for char, count in freq.items()]

    def is_palindrome(self, value):
        """
        Checks if the given string or number is a palindrome.
        """
        original = str(value)
        reversed_str = ''
        for index in range(len(original) - 1, -1, -1):
            reversed_str += original[index]
        return original == reversed_str

    def display_menu(self):
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

    def run(self):
        """
        Runs the interactive CLI program using click.
        """
        while True:
            self.display_menu()

            try:
                choice_input = click.prompt("Enter your choice (0-7)", type=str)
                if choice_input == '7' or choice_input == 'exit':
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
                        user_input = click.prompt("Enter list of numbers (e.g., 10 20 30 or [10, 20, 30])", type=str)
                        if user_input.startswith('[') and user_input.endswith(']'):
                            numbers = list(map(int, user_input.strip('[]').split(',')))
                        else:
                            numbers = list(map(int, user_input.split()))
                        result = self.second_largest(numbers)
                        click.echo(f"Second Largest: {result}")

                    case 2:
                        n = click.prompt("Enter value of n", type=int)
                        self.print_reverse_triangle(n)

                    case 3:
                        inp = click.prompt("Enter a string to swap case", type=str)
                        click.echo("Swapped String: " + self.swap_case(inp))

                    case 4:
                        user_input = click.prompt("Enter characters (e.g., a a b OR ['a','a','b'])", type=str).strip()
                        if user_input.startswith('[') and user_input.endswith(']'):
                            try:
                                chars = literal_eval(user_input)
                            except Exception:
                                click.echo("Invalid list format.")
                                continue
                        else:
                            chars = user_input.split()
                        click.echo(f"Result: {self.count_contiguous_characters(chars)}")

                    case 5:
                        user_input = input("Enter list of numbers (e.g., 1 2 3 4 OR [1, 2, 3, 4]): ").strip()
                        if user_input.startswith('[') and user_input.endswith(']'):
                            try:
                                numbers = literal_eval(user_input)
                                if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
                                    print("Please enter a valid list of integers.")
                                    continue
                            except Exception:
                                print("Invalid list format.")
                                continue
                        else:
                            try:
                                numbers = list(map(int, user_input.split()))
                            except ValueError:
                                print("Please enter a valid space-separated list of integers.")
                                continue
                        try:
                            target_val = int(input("Enter target value: "))
                        except ValueError:
                            print("Please enter a valid integer target.")
                            continue
                        print("Result:", self.find_target_sum_indices(numbers, target_val))

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

            cont = click.prompt("\nDo you want to continue? (yes/no)", type=str)
            if not cont.startswith('y'):
                click.echo("Thank you! Exiting now.")
                break


@click.command()
def main():
    """
    Runs the assessment program with a menu using the click package.

    Returns:
        None
    """
    app = AssessmentProgram()
    app.run()

if __name__ == '__main__':
    main()
