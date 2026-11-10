# POST request
# api url
# https://api.jarvisclaw.ai/v1/chat/completions

# body
# {
#   "model": "auto/free",
#   "messages": [
#     {
#       "role": "user",
#       "content": "What is Python? Explain in two sentences."
#     }
#   ],
#   "stream": false
# }


# from flask import Flask, jsonify, request

# app = Flask(__name__)

# students_dict = {
#     1: {"name": "John", "age": 20},
#     2: {"name": "Jane", "age": 22}
# }

# id_counter = 2

# # PUT, POST, DELETE, PATCH, GET
# @app.get("/hello")
# def hello():
#     a = 3
#     return {"message": "Hello!"}

# # @app.get("/students")
# @app.route("/students", methods=["GET"])
# def students():
#     return jsonify(students_dict)

# @app.route("/create_student", methods=["POST"])
# def create_student():
#     global id_counter
#     id_counter = id_counter + 1
#     print(request.json)
#     students_dict[id_counter] = request.json
#     return jsonify(students_dict)

# @app.route("/students/<int:id>", methods=["PATCH"])
# def update_student(id):
#     students_dict[id].update(request.json)
#     return jsonify(students_dict)

# @app.route("/students/<int:id>", methods=["DELETE"])
# def delete_student(id):
#     students_dict.pop(id, None)
#     # return jsonify({"message": "Deleted"})
#     return jsonify(students_dict)

# app.run(debug=True)

# using tinydb library, to actually store and update data in database



from flask import Flask, jsonify, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('students.json')

# PUT, POST, DELETE, PATCH, GET
@app.get("/hello")
def hello():
    a = 3
    return {"message": "Hello!"}

# @app.get("/students")
@app.route("/students", methods=["GET"])
def students():
    return jsonify(db.all())

@app.route("/create_student", methods=["POST"])
def create_student():
    db.insert(request.json)
    return jsonify(db.all())

@app.route("/students/<int:id>", methods=["PATCH"])
def update_student(id):
    db.update(request.json, doc_ids=[id])
    return jsonify(db.all())

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    db.remove(doc_ids=[id])
    return jsonify(db.all())

app.run(debug=True)
