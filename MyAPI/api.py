from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class MyAPI(Resource):
    def get(self):
        return {
            "items": [  "Ice cream",
                        "Chocolate",
                        "Fruit",
                        "Eggs",
                        "Watter"]
        }
        
api.add_resource(MyAPI, "/")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)