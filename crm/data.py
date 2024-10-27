from models import Customer, Contact, Order, Product
from database import Session
from sqlalchemy.exc import IntegrityError


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def add_customer(name):
    session = Session()
    try:
        customer = Customer(name=name)
        session.add(customer)
        session.commit()
        return customer.id
    except IntegrityError:
        session.rollback()
        print("Error: Customer with this name already exists.")
    finally:
        session.close()


def update_customer(customer_id, new_name):
    session = Session()
    try:
        customer = session.query(Customer).get(customer_id)
        if customer:
            customer.name = new_name
            session.commit()
            print("Customer updated successfully.")
        else:
            print("Error: Customer not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def delete_customer(customer_id):
    session = Session()
    try:
        customer = session.query(Customer).get(customer_id)
        if customer:
            session.delete(customer)
            session.commit()
            print("Customer deleted successfully.")
        else:
            print("Error: Customer not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def print_customer_details(customer_id):
    session = Session()
    try:
        customer = session.query(Customer).filter_by(id=customer_id).first()

        if customer:
            print(f"\nDetails for Customer ID: {customer.id}")
            print(f"Name: {customer.name}")

            print("Contacts:")
            for contact in customer.contacts:
                print(f"- {contact.id}: {contact.name} ({contact.email})")

            print("Orders:")
            for order in customer.orders:
                print(f"- Order ID: {order.id}, Date: {order.date}")
                print("  Products:")
                for product in order.products:
                    print(f"  - {product.name}")
        else:
            print(f"No customer found with ID: {customer_id}")
    except Exception as e:
        print(f"An error occurred while fetching customer details: {e}")
    finally:
        session.close()


def add_contact(customer_id, name, email):
    session = Session()
    try:
        contact = Contact(name=name, email=email, customer_id=customer_id)
        session.add(contact)
        session.commit()
        print("Contact added successfully.")
    except IntegrityError:
        session.rollback()
        print("Error: Contact with this email already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def add_order(customer_id, date):
    session = Session()
    try:
        order = Order(date=date, customer_id=customer_id)
        session.add(order)
        session.commit()
        return order.id
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def add_product(name):
    session = Session()
    try:
        product = Product(name=name)
        session.add(product)
        session.commit()
        return product.id
    except IntegrityError:
        session.rollback()
        print("Error: Product with this name already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def add_product_to_order(order_id, product_id):
    session = Session()
    try:
        order = session.query(Order).get(order_id)
        product = session.query(Product).get(product_id)
        if order and product:
            if product in order.products:
                print(f"Error: Product ID: {product_id} is already in Order ID: {order_id}.")
            else:
                order.products.append(product)
                session.commit()
                print(f"Added Product ID: {product_id} to Order ID: {order_id}")
        else:
            print("Error: Order or Product not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()
