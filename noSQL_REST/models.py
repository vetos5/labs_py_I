def create_customer(mongo, data):
    customer_id = mongo.db.customers.insert_one(data).inserted_id
    return str(customer_id)


def create_interaction(mongo, data):
    interaction_id = mongo.db.interactions.insert_one(data).inserted_id
    return str(interaction_id)
