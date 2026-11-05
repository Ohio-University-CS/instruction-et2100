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


from flask import Flask, jsonify, request

app = Flask(__name__)

students_dict = {
    1: {"name": "John", "age": 20},
    2: {"name": "Jane", "age": 22}
}

id_counter = 2

# PUT, POST, DELETE, PATCH, GET
@app.get("/hello")
def hello():
    a = 3
    return {"message": "Hello!"}

# @app.get("/students")
@app.route("/students", methods=["GET"])
def students():
    return jsonify(students_dict)

@app.route("/create_student", methods=["POST"])
def create_student():
    global id_counter
    id_counter = id_counter + 1
    print(request.json)
    students_dict[id_counter] = request.json
    return jsonify(students_dict)

app.run(debug=True)






# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Simple in-memory database
# students = {
#     1: {"name": "Alice", "age": 20},
#     2: {"name": "Bob", "age": 22}
# }

# # GET - Read all students
# @app.route("/students", methods=["GET"])
# def get_students():
#     return jsonify(students)

# # POST - Create a student
# @app.route("/students/<int:id>", methods=["POST"])
# def create_student(id):
#     students[id] = request.json
#     return jsonify(students[id]), 201

# # PUT - Replace a student
# @app.route("/students/<int:id>", methods=["PUT"])
# def replace_student(id):
#     students[id] = request.json
#     return jsonify(students[id])

# # PATCH - Update part of a student
# @app.route("/students/<int:id>", methods=["PATCH"])
# def update_student(id):
#     students[id].update(request.json)
#     return jsonify(students[id])

# # DELETE - Delete a student
# @app.route("/students/<int:id>", methods=["DELETE"])
# def delete_student(id):
#     students.pop(id, None)
#     return jsonify({"message": "Deleted"})

# app.run(debug=True)