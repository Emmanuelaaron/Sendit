from flask import Flask


app = Flask(__name__)
@app.route("/")
def index():
    return "Do you wanna send it?, if yes send it"