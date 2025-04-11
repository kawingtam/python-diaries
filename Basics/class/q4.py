4. Create a BankAccount Class
Objective: Create a class to simulate a basic bank account.

Requirements:

Initialize the account with an account holder's name and balance.

Add methods deposit(amount) to deposit money into the account, and withdraw(amount) to withdraw money.

Ensure that the balance does not go below 0.

Example Output:

python
Copy code
account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # Output: 1300