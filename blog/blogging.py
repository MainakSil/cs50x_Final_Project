from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from cs50 import SQL

from .helpers import apology, login_required

# Initiate blueprint variable
bp = Blueprint("blogging", __name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///blog/database/blog.db")


def get_user_data():
    # Get the logged in user's data
    user_id = session["user_id"]
    user_data = db.execute("SELECT * FROM users WHERE id = ?;", user_id)[0]

    return user_data


def create_posts_table():
    # Create table for posts if the table does not exist
    db.execute(
        "CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, timestamp DATETIME NOT NULL);"
    )


@bp.route("/")
@login_required
def index():
    """Show home page"""

    # Get the logged in user's data
    user = get_user_data()
    # Get the logged in user's posts, limited to the 3 latest posts
    create_posts_table()
    posts = db.execute(
        "SELECT * FROM posts WHERE user_id = ? ORDER BY id DESC LIMIT 3;",
        user["id"]
    )

    return render_template("blogging/index.html", user=user, posts=posts)


def get_post(post_id):
    try:
        # Get the individual post's data by ID
        post = db.execute("SELECT * FROM posts WHERE id = ?;", post_id)[0]
        return post
    except (IndexError):
        return None


@bp.route("/posts/<int:post_id>", methods=["GET"])
@login_required
def post(post_id):
    """Individual blog post page"""
    post = get_post(post_id)

    # Display apology if the post does not exist
    if post is None:
        return apology("post not found", 404)

    # Get the logged in user's data
    user = get_user_data()

    # Render the post page
    return render_template("blogging/post.html", post=post, user=user)


@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    """Create new blog post"""
    # User reached route via GET (as by clicking the "Buy" link)
    if request.method == "GET":
        return render_template("blogging/create.html")

    # User reached route via POST (as by submitting the quote form)
    elif request.method == "POST":
        # Get input data
        post_title = request.form.get("post-title")
        post_content = request.form.get("ckeditor")

        # Ensure post title and post content are provided
        if not post_title:
            return apology("must enter a post title", 400)
        elif not post_content:
            return apology(
                "must enter blog content", 400
            )
        else:
            # Get the logged in user's ID
            user_id = session["user_id"]

            create_posts_table()

            # Insert the post into the posts table
            db.execute(
                "INSERT INTO posts (user_id, title, content, timestamp) VALUES(?, ?, ?, datetime('now', 'localtime'));",
                user_id, post_title, post_content,
            )

            # Redirect user back to the home page
            flash(
                f'You have successfully created a new post: "{post_title}".'
            )
            return redirect(url_for(".index"))


@bp.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    """Edit a blog post"""
    # Get the post's ID
    post = get_post(post_id)

    if request.method == "POST":
        # Get input data
        post_title = request.form.get("post-title")
        post_content = request.form.get("ckeditor")

        if not post_title:
            flash('Title is required!')
        else:
            # Update the table
            db.execute(
                "UPDATE posts SET title = ?, content = ? WHERE id = ?;",
                post_title, post_content, post_id,
            )
            flash(
                f'You have successfully edited the post, "{post_title}".'
            )
            return redirect(url_for(".index"))

    return render_template("blogging/edit.html", post=post)


@bp.route('/<int:post_id>/delete', methods=["POST"])
@login_required
def delete_post(post_id):
    """Delete a blog post"""
    # Get the post's data
    post = get_post(post_id)

    # Remove the post from the posts table
    db.execute("DELETE FROM posts WHERE id = ?;", post_id)

    flash(
        f'You have successfully deleted the post, "{post["title"]}".'
    )
    return redirect(url_for(".index"))


@bp.route("/posts", methods=["GET"])
@login_required
def posts():
    """Blog post archive"""

    # Get the logged in user's data
    user = get_user_data()
    # Get the logged in user's posts
    create_posts_table()
    posts = db.execute(
        "SELECT * FROM posts WHERE user_id = ? ORDER BY id DESC;",
        user["id"]
    )

    return render_template("blogging/posts.html", user=user, posts=posts)
