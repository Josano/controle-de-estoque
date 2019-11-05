from flask_restful import Resource

from app.models.product import Product as ProductModel


class Product(Resource):
    def get(self):
        product = ProductModel.query.all();
        return product

    def post(self):
        pass