from flask import Flask, request

# Create app 
app = Flask(__name__)

# Routing

# Index route to "/"
# @ is a decorator that extends a function or class
@app.get("/")
def index():
    return "Hello World!"

@app.get("/param/<my_param>")
def param(my_param):
    # access a url query
    # /param/INSERTPARAMETER?query=somethingelse
    query = request.args.get("query", None)
    return {"param": my_param, "query": query}

# Server Run like app.listen in Express
app.run(host="localhost", port=3000)