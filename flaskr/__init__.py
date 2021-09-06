import os
from flask import render_template
from flask import Flask, flash, request, redirect, url_for
from .app import *

from werkzeug.utils import secure_filename

def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def render():
        return render_template(
            "discovar.html"
        )


    @app.route("/upload-image", methods=["GET", "POST"])
    def upload_image():
        if request.method == "POST":
            if request.files:
                image = request.files["userInput"]
                image.save(os.path.join(os.getcwd(), image.filename))
                global result
                result = detect_landmarks(image.filename)
                return redirect(request.url)

        return render_template("upload_image.html", landmark=result[0], summary=result[1])

    return app