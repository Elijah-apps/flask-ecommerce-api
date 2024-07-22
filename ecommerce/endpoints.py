from flask_restful import Resource, reqparse

products = {}
orders = {}
customers = {}

# Product Endpoints
class ProductList(Resource):
    def get(self):
        return products, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('stock', type=int, required=True)
        args = parser.parse_args()
        product_id = str(len(products) + 1)
        products[product_id] = args
        return products[product_id], 201

class ProductDetail(Resource):
    def get(self, product_id):
        if product_id in products:
            return products[product_id], 200
        return "Product not found", 404

    def put(self, product_id):
        if product_id in products:
            parser = reqparse.RequestParser()
            parser.add_argument('name')
            parser.add_argument('price', type=float)
            parser.add_argument('stock', type=int)
            args = parser.parse_args()
            products[product_id].update(args)
            return products[product_id], 200
        return "Product not found", 404

    def delete(self, product_id):
        if product_id in products:
            del products[product_id]
            return '', 200
        return "Product not found", 404

# Order Endpoints
class OrderList(Resource):
    def get(self):
        return orders, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', required=True)
        parser.add_argument('quantity', type=int, required=True)
        parser.add_argument('customer_id', required=True)
        args = parser.parse_args()
        order_id = str(len(orders) + 1)
        orders[order_id] = args
        return orders[order_id], 201

class OrderDetail(Resource):
    def get(self, order_id):
        if order_id in orders:
            return orders[order_id], 200
        return "Order not found", 404

    def put(self, order_id):
        if order_id in orders:
            parser = reqparse.RequestParser()
            parser.add_argument('product_id')
            parser.add_argument('quantity', type=int)
            parser.add_argument('customer_id')
            args = parser.parse_args()
            orders[order_id].update(args)
            return orders[order_id], 200
        return "Order not found", 404

    def delete(self, order_id):
        if order_id in orders:
            del orders[order_id]
            return '', 200
        return "Order not found", 404

# Customer Endpoints
class CustomerList(Resource):
    def get(self):
        return customers, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('address', required=True)
        args = parser.parse_args()
        customer_id = str(len(customers) + 1)
        customers[customer_id] = args
        return customers[customer_id], 201

class CustomerDetail(Resource):
    def get(self, customer_id):
        if customer_id in customers:
            return customers[customer_id], 200
        return "Customer not found", 404

    def put(self, customer_id):
        if customer_id in customers:
            parser = reqparse.RequestParser()
            parser.add_argument('name')
            parser.add_argument('email')
            parser.add_argument('address')
            args = parser.parse_args()
            customers[customer_id].update(args)
            return customers[customer_id], 200
        return "Customer not found", 404

    def delete(self, customer_id):
        if customer_id in customers:
            del customers[customer_id]
            return '', 200
        return "Customer not found", 404
