from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'customers'
app.config['MONGO_URI'] = "mongodb://localhost:27017/customers"

mongo = PyMongo(app)


@app.route('/mongodb', methods=['GET'])
class MongoDB:




    def findd(self):
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print(client.list_database_names())
        db = client["customersdb"]
        customers = db["customers"]
        for x in customers.find():
            print(x)

    def __repr__(self) -> None:
        return x

@app.route("/")
def hello_world():
    return render_template('index.html')
  #  return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "This is product page"

if __name__ == '__main__':
    app.run(debug=True)
