import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.db import stores
from src.schemas import StoreSchema

StoresRoute = Blueprint("Stores", __name__, description="Operation on stores")


@StoresRoute.route("/store/<string:store_id>")
class Store(MethodView):
    @StoresRoute.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found!")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted!"}
        except KeyError:
            abort(404, message="Store not found!")


@StoresRoute.route("/store")
class StoreList(MethodView):
    @StoresRoute.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @StoresRoute.arguments(StoreSchema)
    @StoresRoute.response(200, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists!")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store
