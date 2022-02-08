from flask import Flask
from routes import init

app = Flask(__name__)

if __name__ == "__main__":
    init(app=app)
    app.run(host="0.0.0.0", port=4000, debug=True)