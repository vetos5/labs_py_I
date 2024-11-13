import random
import threading
from models import BankAccount


def user_activity(account):
    for _ in range(5):
        operation = random.choice(['replenishment', 'withdrawal'])
        amount = random.randint(10, 100)
        account.update_balance(amount if operation == 'replenishment' else -amount, operation)


def run_threads():
    account = BankAccount(100)
    users = []

    for i in range(5):
        user_thread = threading.Thread(target=user_activity, args=(account,), name=f"User {i + 1}")
        users.append(user_thread)
        user_thread.start()

    for user in users:
        user.join()

    print(f"Balance: {account.get_balance()}")


if __name__ == "__main__":
    run_threads()
