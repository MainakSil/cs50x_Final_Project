from flask import Flask
from flask_session import Session
from flask_ckeditor import CKEditor

from blog import auth, blogging, account, info

ckeditor = CKEditor()

def create_app():
    app = Flask(__name__)

    ckeditor.init_app(app)

    # Configure session to use filesystem (instead of signed cookies)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    @app.after_request
    def after_request(response):
        """Ensure responses aren't cached"""
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    app.register_blueprint(auth.bp)
    app.register_blueprint(blogging.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(info.bp)

    return app