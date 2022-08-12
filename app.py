from flask import Flask

app = Flask(__name__)

store = [
    {
        'name': 'Zekrom Store',
        'items': [
            {
                'name': 'Random Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store')
def get_stores(name):
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)

# POST - used to receive data
# GET - used to send data back only
