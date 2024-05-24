from flask import Blueprint, render_template, session, flash, redirect, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL

from .helpers import apology

# Initiate blueprint variable
bp = Blueprint("auth", __name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///blog/database/blog.db")


def create_users_table():
    # Create table for users if the table does not exist
    db.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL);"
    )


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        create_users_table()

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?;", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("You have successfully logged in.")
        return redirect(url_for("blogging.index"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    flash("You have successfully logged out.")
    return redirect(url_for('blogging.index'))


@bp.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via GET (as by clicking the "Register" link)
    if request.method == "GET":
        return render_template("auth/register.html")

    # User reached route via POST (as by submitting the registration form)
    elif request.method == "POST":
        # Get input data
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        create_users_table()

        # Query database for username
        user_row = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username was provided
        if not username:
            return apology("must provide username", 400)
        # Check if username is already taken
        elif len(user_row) == 1:
            return apology("username is already taken", 400)
        # Ensure password was provided
        elif not password:
            return apology("must provide password", 400)
        elif not confirmation:
            return apology("must confirm password", 400)
        elif confirmation != password:
            return apology("password and confirmation must match", 400)
        else:
            create_users_table()

            # Insert data into database
            db.execute(
                "INSERT INTO users (username, password) VALUES(?, ?);",
                username,
                generate_password_hash(password),
            )

            # Set user's log-in session
            session["user_id"] = db.execute(
                "SELECT * FROM users WHERE username = ?;", username
            )[0]["id"]

            # Redirect user to home page
            flash("You have successfully registered an account.")
            return redirect(url_for("blogging.index"))
