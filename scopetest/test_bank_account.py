import pytest
from bank_account import get_account_balance, set_account_balance, BankAccount, deposit_to_global_account

# Test Case 1: Test the module-level account balance
#The fixture will run once per test module (i.e., before any tests in this file are executed, and after all tests are completed).
@pytest.fixture(scope="module")
def setup_module_balance():
    """Setup initial module balance."""
    set_account_balance(1000)  # Set initial balance
    yield
    set_account_balance(1000)  # Reset balance after tests

def test_module_balance_initial(setup_module_balance):
    """Test the initial balance."""
    assert get_account_balance() == 1000, "Initial balance should be 1000"

def test_module_balance_deposit(setup_module_balance):
    """Test depositing into the module balance."""
    new_balance = deposit_to_global_account(500)
    assert new_balance == 1500, "Balance should be 1500 after deposit"

# Test Case 2: Test the BankAccount class and its methods
#The fixture will run once per test class (i.e., before any tests in the class run, and after all tests in the class are done).
@pytest.fixture(scope="class")
def setup_class_balance():
    """Setup initial class balance for user."""
    yield BankAccount("John Doe")  # Setup a user account with initial balance 500

def test_class_balance_initial(setup_class_balance):
    """Test the initial balance of a class-based account."""
    user_account = setup_class_balance
    assert user_account.balance == 500, "User balance should be 500 initially"

def test_class_balance_deposit(setup_class_balance):
    """Test depositing money into the class-based user account."""
    user_account = setup_class_balance
    new_balance = user_account.deposit(200)
    assert new_balance == 700, "User balance should be 700 after deposit"

def test_class_balance_withdraw(setup_class_balance):
    """Test withdrawing money from the class-based user account."""
    user_account = setup_class_balance
    new_balance = user_account.withdraw(100)
    assert new_balance == 400, "User balance should be 400 after withdrawal"

# Test Case 3: Test function-level deposit to the global account
def test_function_balance_deposit():
    """Test the deposit function for the global account."""
    new_balance = deposit_to_global_account(300)
    assert new_balance == 1800, "Global account balance should be 1800 after deposit"
