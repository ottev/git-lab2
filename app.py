from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "Hello, World!"

@app.get("/about")
def about():
    return "About this laboratory project"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)