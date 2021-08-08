import os
import re
from flask import Flask, flash, render_template, request, redirect, url_for
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

    @app.route('/', methods=["GET", "POST"])
    def render():

        if request.method == "POST":
            if request.files:

                image = request.files["userInput"]

                image.save(os.path.join(os.getcwd(), image.filename))

                return redirect(request.url)

        return render_template(
            "discovar.html"
        )

    return app