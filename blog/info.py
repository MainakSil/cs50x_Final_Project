from flask import Blueprint, render_template


# Initiate blueprint variable
bp = Blueprint("info", __name__)


@bp.route("/about", methods=["GET"])
def about():
    return render_template("info/about.html")
