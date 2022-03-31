from flask import Flask

# Create app 
app = Flask(__name__)

# Routing

# Index route to "/"
# @ is a decorator that extends a function or class
@app.route("/")
def index():
    return "Hello World!"

# Server Run like app.listen in Express
app.run(host="localhost", port=3000)