import sqlite3

from creds import *
from simple_salesforce import Salesforce, SalesforceError
from simple_salesforce.exceptions import SalesforceMalformedRequest, SalesforceGeneralError, SalesforceResourceNotFound


def exportContactsToSqlite():
    try:
        sf = Salesforce(username=username,
                        password=password,
                        security_token=security_token)
    except SalesforceError as e:
        print('Could not authenticate with Salesforce')
        print(f"Error: {e}")
        exit(1)

    try:
        conn = sqlite3.connect('salesforce_data.db')
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print("Could not connect to SQLite database.")
        print(f"Error: {e}")
        exit(1)

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
    ''')

    try:
        contacts = sf.query_all("SELECT Id, FirstName, LastName, Email "
                                "FROM Contact")
    except (SalesforceMalformedRequest, SalesforceResourceNotFound) as e:
        print("Error querying Salesforce.")
        print(f"Error: {e}")
        exit(1)
    except SalesforceGeneralError as e:
        print("An error occurred with the Salesforce API.")
        print(f"Error: {e}")
        exit(1)

    for contact in contacts['records']:
        cursor.execute('''
        INSERT OR REPLACE INTO contacts (id, first_name, last_name, email)
        VALUES (?, ?, ?, ?)''',
                       (contact['Id'], contact['FirstName'], contact['LastName'], contact['Email']))

    try:
        conn.commit()
        print('Successfully committed changes.')
    except sqlite3.IntegrityError:
        conn.rollback()
        print('Failed to commit changes.')
        exit(1)
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")

    print("Export successfully finished!")
