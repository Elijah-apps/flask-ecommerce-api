from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from ecommerce.endpoints import ProductList, ProductDetail, OrderList, OrderDetail, CustomerList, CustomerDetail

app = Flask(__name__)
api = Api(app)

# Add API endpoints
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')
api.add_resource(OrderList, '/orders')
api.add_resource(OrderDetail, '/orders/<string:order_id>')
api.add_resource(CustomerList, '/customers')
api.add_resource(CustomerDetail, '/customers/<string:customer_id>')

# Swagger UI setup
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "E-commerce API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
