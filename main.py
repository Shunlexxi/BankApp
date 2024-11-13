class Account:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} has been deposited to your account.")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"${amount} has been withdrawn from your account.")
        else:
            print("Insufficient balance or invalid amount.")

    def send_money(self, recipient, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Sent: ${amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received: ${amount} from {self.name}")
            print(f"${amount} has been sent to {recipient.name}.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def show_transaction_history(self):
        if self.transaction_history:
            print(f"Transaction history for {self.name}:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transaction history available.")


# Main program

user = input('Enter your name: ')
greetings = f'Hello, {user}!, Welcome to the Bank App.\nHow can we help you today?'
line_break = '==============================='
service = '1. Create an account\n2. Deposit\n3. Send Money\n4. Check Balance\n5. Transaction History\n6. Exit'


print(greetings)
print(line_break)
print(service)





# Example Usage
# Creating accounts
account1 = Account("Alice", 100)
account2 = Account("Bob", 50)

# Depositing money
account1.deposit(50)

# Withdrawing money
account1.withdraw(30)

# Sending money
account1.send_money(account2, 20)

# Displaying balance
account1.show_balance()
account2.show_balance()

# Showing transaction history
account1.show_transaction_history()
account2.show_transaction_history()
