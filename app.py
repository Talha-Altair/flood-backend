from flask import Flask
from routes import api
from settings import HOST, PORT

app = Flask(__name__)

app.register_blueprint(api.api)

if __name__ == "__main__":

    app.run(
        host=HOST,
        port=PORT,
        debug=True
    )