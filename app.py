
import os
from flask import Flask, render_template, jsonify
from config import Config
from routes.api import api
from werkzeug.exceptions import RequestEntityTooLarge

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    folders = [
        app.config["FACE_FOLDER"],
        app.config["VIDEO_FOLDER"],
        app.config["OUTPUT_FOLDER"]
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    app.register_blueprint(api)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.errorhandler(RequestEntityTooLarge)
    def file_too_large(error):
        return jsonify({
            "error": "Upload is too large. Maximum size is 110 MB."
        }), 413

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
