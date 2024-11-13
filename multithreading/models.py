# models.py
import sqlite3
import threading
from datetime import datetime


class BankAccount:
    def __init__(self, initial_balance=0):
        self.lock = threading.Lock()
        self.connection = sqlite3.connect("bank_account.db", check_same_thread=False)
        self.create_table()
        self.set_balance(initial_balance)

    def create_table(self):
        with self.connection:
            self.connection.execute("CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, balance INTEGER)")
            # Initialize with default balance if table is empty
            if not self.get_balance():
                self.connection.execute("INSERT INTO account (balance) VALUES (0)")

    def get_balance(self):
        result = self.connection.execute("SELECT balance FROM account WHERE id = 1").fetchone()
        return result[0] if result else 0

    def set_balance(self, balance):
        with self.connection:
            self.connection.execute("UPDATE account SET balance = ? WHERE id = 1", (balance,))

    def log_transaction(self, operation, amount, success):
        with open("transaction_log.txt", "a") as f:
            f.write(
                f"{datetime.now()} - {threading.current_thread().name} - {operation} Amount: {amount}. Success: {success}. Current balance: {self.get_balance()}\n")

    def update_balance(self, amount, operation):
        with self.lock:
            print(f"{threading.current_thread().name} processing operation '{operation}' Amount: {abs(amount)}")
            current_balance = self.get_balance()
            new_balance = current_balance + amount if operation == 'replenishment' else current_balance - amount

            if new_balance < 0:
                print(f"{threading.current_thread().name}: Insufficient funds for {abs(amount)}.")
                self.log_transaction(operation, amount, success=False)
            else:
                self.set_balance(new_balance)
                print(f"{threading.current_thread().name} completed operation '{operation}'. Current balance: {new_balance}")
                self.log_transaction(operation, amount, success=True)
