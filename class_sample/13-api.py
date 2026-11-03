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


from flask import Flask

app = Flask(__name__)

@app.get("/hello")
def hello():
    return {"message": "Hello!"}

app.run(debug=True)

