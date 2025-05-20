from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

courses = {
    1: {"name": "Math", "price": 100},
    2: {"name": "Science", "price": 200},
    3: {"name": "History", "price": 300},
    4: {"name": "English", "price": 400},
    5: {"name": "Spanish", "price": 500},
}

class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        return courses[course_id]
    
    def post(self, course_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("price", type=int)
        courses[course_id] = parser.parse_args()
        return courses

    def put(self, course_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("price", type=int)
        courses[course_id] = parser.parse_args()
        return courses
    
    def delete(self, course_id):
        del courses[course_id]
        return courses
    
api.add_resource(Main, "/<int:course_id>")
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")