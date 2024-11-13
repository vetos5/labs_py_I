from datetime import datetime


def log_transaction_to_file(operation, amount, success, current_balance):

    with open("transaction_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {operation} Amount: {amount}. Success: {success}. Current balance: {current_balance}\n")
