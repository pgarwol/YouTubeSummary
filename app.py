from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello world </h1>"


@app.route("/get_movie_info/<name>", methods=["POST"])
def get_movie_info(name: str):
    return f"Movieeee"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2137, debug=True)
