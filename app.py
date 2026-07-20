from flask import Flask, request, jsonify
from calculator import add

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(status="ok")


@app.route("/add")
def add_route():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
    except ValueError:
        return jsonify(error="invalid numbers"), 400
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
