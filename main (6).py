# 2.1 Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.

class BankAccount:
  def __init__(self, account_number: str, account_holder_name: str, account_balance: float):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = account_balance

  def deposit(self, amount: float) -> None:
      self.__account_balance += amount

  def withdraw(self, amount: float) -> None:
      if amount > self.__account_balance:
          raise ValueError("Insufficient balance")
      self.__account_balance -= amount

  def display_balance(self) -> float:
      return self.__account_balance

# Create a new bank account with an initial balance of 1000
my_account = BankAccount("123456789", "John Doe", 1000)

# Deposit 500 into the account
my_account.deposit(500)

# Withdraw 200 from the account
my_account.withdraw(200)

# Display the current balance of the account
print("Current balance:", my_account.display_balance())