from flask import jsonify, request
from bson import ObjectId
from pymongo.errors import WriteError, DuplicateKeyError


def register_routes(app, mongo):
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the CRM API!"}), 200

    @app.route('/customers', methods=['POST'])
    def create_customer():
        data = request.json
        try:
            customer_id = mongo.db.customers.insert_one(data).inserted_id
            return jsonify({"id": str(customer_id), **data}), 201
        except DuplicateKeyError:
            return jsonify({'error': 'Customer already exists'}), 400
        except WriteError:
            return jsonify({'error': 'Error creating customer'}), 500

    @app.route('/customers', methods=['GET'])
    def get_all_customers():
        customers = list(mongo.db.customers.find())
        for customer in customers:
            customer['_id'] = str(customer['_id'])
        return jsonify(customers), 200

    @app.route('/customers/<customer_id>', methods=['GET'])
    def get_customer(customer_id):
        try:
            customer = mongo.db.customers.find_one({'_id': ObjectId(customer_id)})
            if not customer:
                return jsonify({'error': 'Customer not found'}), 404
            customer['_id'] = str(customer['_id'])
            return jsonify(customer), 200
        except Exception:
            return jsonify({'error': 'Invalid customer ID format'}), 400

    @app.route('/customers/<customer_id>', methods=['PATCH'])
    def update_customer(customer_id):
        data = request.json
        try:
            result = mongo.db.customers.update_one({'_id': ObjectId(customer_id)}, {'$set': data})
            if result.matched_count == 0:
                return jsonify({'error': 'Customer not found'}), 404
            return jsonify({'result': 'Customer updated'}), 200
        except Exception:
            return jsonify({'error': 'Invalid customer ID format'}), 400

    @app.route('/customers/<customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        try:
            result = mongo.db.customers.delete_one({'_id': ObjectId(customer_id)})
            if result.deleted_count == 0:
                return jsonify({'error': 'Customer not found'}), 404
            return jsonify({'result': 'Customer deleted'}), 204
        except Exception:
            return jsonify({'error': 'Invalid customer ID format'}), 400

    @app.route('/interactions', methods=['POST'])
    def create_interaction():
        data = request.json
        try:
            interaction_id = mongo.db.interactions.insert_one(data).inserted_id
            return jsonify({"id": str(interaction_id), **data}), 201
        except WriteError:
            return jsonify({'error': 'Error creating interaction'}), 500

    @app.route('/interactions/<customer_id>', methods=['GET'])
    def get_interactions(customer_id):
        try:
            interactions = list(mongo.db.interactions.find({'customer_id': ObjectId(customer_id)}))
            for interaction in interactions:
                interaction['_id'] = str(interaction['_id'])
            return jsonify(interactions), 200
        except Exception:
            return jsonify({'error': 'Invalid customer ID format'}), 400
