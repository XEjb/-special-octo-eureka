"""Simple Flask."""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    """Simple Flask method."""
    return "Hello"


@app.route('/add')
def add():
    return str(request.args.get("a")) + request.args.get("b")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
