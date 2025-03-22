import os
import random
import time
import json

class Account:
    def __init__(self, name, balance=0, acc_type='SAVINGS'):
        self.name = name
        self.acc_no = random.randint(10000, 99999)
        self.balance = balance
        self.acc_type = acc_type

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def display(self):
        print(f"Account Number: {self.acc_no}, Name: {self.name}, Balance: {self.balance}, Type: {self.acc_type}")

class Bank:
    def __init__(self, filename='accounts.json'):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_accounts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.accounts, file, indent=4)

    def create_account(self, name, acc_type):
        acc = Account(name, acc_type=acc_type)
        self.accounts[acc.acc_no] = {'name': acc.name, 'balance': acc.balance, 'acc_type': acc.acc_type}
        self.save_accounts()
        print(f"Account created! Account No: {acc.acc_no}")
        return acc.acc_no

    def deposit(self, acc_no, amount):
        if str(acc_no) in self.accounts:
            self.accounts[str(acc_no)]['balance'] += amount
            self.save_accounts()
            print("Deposit successful!")
        else:
            print("Account not found!")

    def withdraw(self, acc_no, amount):
        if str(acc_no) in self.accounts and self.accounts[str(acc_no)]['balance'] >= amount:
            self.accounts[str(acc_no)]['balance'] -= amount
            self.save_accounts()
            print("Withdrawal successful!")
        else:
            print("Insufficient funds or invalid account!")

    def display_account(self, acc_no):
        if str(acc_no) in self.accounts:
            acc = self.accounts[str(acc_no)]
            print(f"Account No: {acc_no}, Name: {acc['name']}, Balance: {acc['balance']}, Type: {acc['acc_type']}")
        else:
            print("Account not found!")

    def transfer(self, from_acc, to_acc, amount):
        if str(from_acc) in self.accounts and str(to_acc) in self.accounts:
            if self.accounts[str(from_acc)]['balance'] >= amount:
                self.accounts[str(from_acc)]['balance'] -= amount
                self.accounts[str(to_acc)]['balance'] += amount
                self.save_accounts()
                print("Transfer successful!")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid account details!")

if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Display Account\n6. Exit")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            name = input("Enter Name: ")
            acc_type = input("Enter Account Type (SAVINGS/CURRENT): ")
            bank.create_account(name, acc_type)
        elif choice == 2:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount: "))
            bank.deposit(acc_no, amount)
        elif choice == 3:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount: "))
            bank.withdraw(acc_no, amount)
        elif choice == 4:
            from_acc = input("Enter Your Account Number: ")
            to_acc = input("Enter Recipient Account Number: ")
            amount = float(input("Enter Amount: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == 5:
            acc_no = input("Enter Account Number: ")
            bank.display_account(acc_no)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
