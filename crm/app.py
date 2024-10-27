from database import init_db
from data import (
    add_customer,
    update_customer,
    delete_customer,
    add_contact,
    add_order,
    add_product,
    add_product_to_order,
    print_customer_details
)


def main():
    init_db()

    add_customer('Customer_test')

    print_customer_details(2)
    add_contact(2, 'CustomerA', 'customerA@invalid.com')
    print_customer_details(2)

    update_customer(2, 'CustomerA_upd')
    print_customer_details(2)

    add_product_to_order(4, 3)
    delete_customer(2)
    print_customer_details(2)


if __name__ == '__main__':
    main()
