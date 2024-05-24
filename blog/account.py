from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL

from .helpers import apology, login_required

# Initiate blueprint variable
bp = Blueprint("account", __name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///blog/database/blog.db")


def get_user():
    """Get logged in user's data"""
    user_id = session["user_id"]
    user = db.execute("SELECT * FROM users WHERE id = ?;", user_id)[0]

    return user


@bp.route("/account", methods=["GET"])
@login_required
def account():
    """User account settings"""

    # Get the logged in user's data
    user_id = session["user_id"]
    user = db.execute("SELECT * FROM users WHERE id = ?;", user_id)[0]
    username = user["username"]

    return render_template("account/account.html", username=username)


@bp.route("/change_username", methods=["GET", "POST"])
@login_required
def change_username():
    """Change username"""

    # Get the logged in user's data
    user_id = session["user_id"]
    user = db.execute("SELECT * FROM users WHERE id = ?;", user_id)[0]
    username = user["username"]

    # User reached route via POST (as by submitting a form)
    if request.method == "POST":
        # Get input data
        new_username = request.form.get("new-username")

        # Ensure current and new passwords were provided
        if not new_username:
            return apology("must enter new password", 400)
        else:
            # Update user password in theusers table
            db.execute(
                "UPDATE users SET username = ? WHERE id = ?;",
                new_username, user_id,
            )

            # Redirect user to the home page
            flash(f"You have successfully changed your username to {new_username}.")
            return redirect(url_for("blogging.index"))


@bp.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change user password"""

    # Get the logged in user's data
    user_id = session["user_id"]
    user = db.execute("SELECT * FROM users WHERE id = ?;", user_id)[0]
    user_password = user["password"]

    # User reached route via POST (as by submitting a form)
    if request.method == "POST":
        # Get input data
        current_password = request.form.get("current-password")
        new_password = request.form.get("new-password")
        new_confirmation = request.form.get("new-confirmation")

        # Ensure current and new passwords were provided
        if not current_password:
            return apology("must enter current password", 400)
        elif not new_password:
            return apology("must provide new password", 400)
        elif not new_confirmation:
            return apology("must confirm new password", 400)
        # Ensure current password is correct
        elif not check_password_hash(user_password, current_password):
            return apology("invalid password", 403)
        elif new_confirmation != new_password:
            return apology("new password and confirmation must match", 400)
        else:
            # Update user password in theusers table
            db.execute(
                "UPDATE users SET password = ? WHERE id = ?;",
                generate_password_hash(new_password),
                user_id,
            )

            # Redirect user to the home page
            flash("You have successfully changed your password.")
            return redirect(url_for("blogging.index"))
