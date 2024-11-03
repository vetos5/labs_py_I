from flask import Flask
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)


def seed_data():
    customers = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "company": "Example Corp"
        },
        {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "0987654321",
            "company": "Sample Inc"
        },
        {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "phone": "5555555555",
            "company": "Test LLC"
        }
    ]

    mongo.db.customers.insert_many(customers)

    interactions = [
        {
            "customer_id": "1",
            "date": "2024-01-01",
            "notes": "Initial contact with customer."
        },
        {
            "customer_id": "2",
            "date": "2024-01-02",
            "notes": "Follow-up email sent."
        },
        {
            "customer_id": "1",
            "date": "2024-01-03",
            "notes": "Phone call made."
        }
    ]

    mongo.db.interactions.insert_many(interactions)


if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print("Sample data inserted into MongoDB.")
