import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.db import items, stores
from src.schemas import ItemSchema, ItemUpdateSchema

ItemsRoute = Blueprint("Items", __name__, description="Operation on Items")


@ItemsRoute.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found!")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted!"}
        except KeyError:
            abort(404, message="Item not found!")

    @ItemsRoute.arguments(ItemUpdateSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found!")


@ItemsRoute.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"stores": list(items.values())}

    @ItemsRoute.arguments(ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if (
                    item_data["name"] == item["store_id"]
                    and item_data["store_id"] == item["store_id"]
            ):
                abort(404, message=f"Item already exists!")
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found!")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item
