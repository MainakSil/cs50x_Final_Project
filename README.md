# CS50 Flask Blog

A private blogging application built with Flask. My final project for [CS50’s Introduction to Computer Science 2024](https://cs50.harvard.edu/x/2024/project/).



## Demo

Watch it: https://youtu.be/oietie4MTpk


## Description

CS50 Flask Blog is a blogging application designed for private use. Built with Flask and stylised with Bootstrap, CS50 Flask Blog allows users to write and store posts on a local machine.

### Features
- Create user account with password
- Write, edit and delete blog posts
- Rich text editor for writing and editing blog posts
- Change username and password

## Dependencies
- cs50
- Flask
- Flask-CKEditor
- Flask-Session
- Werkzeug

## Running Locally

Requires Python to be installed first.

1. Clone this repository locally
    ```
    git clone https://github.com/MainakSil/cs50x_Final_Project.git
    cd cs50x_Final_Project
    ```

1. Create Python virtual environment
    ```
    python -m venv venv
    ```

1. Activate Python virtual environment

    Windows:
    ```
    .\venv\Scripts\activate
    ```
    Mac/Linux:
    ```
    source venv/bin/activate
    ```

1. Install dependencies
    ```
    pip install -r requirements.txt
    ```

1. Run the project
    ```
    flask --app blog run
    ```

## Project Files

CS50 Flask Blog is built by utilising Flask Blueprints to make the application scalable and easy to maintain. The application files are stored in the main app folder `blog/`.

The root folder of CS50 Flask Blog contains `requirements.txt`, a list of dependency packages of the project.

The `blog/` folder contains the following Python files for the Flask application:
- `__init__.py`: For initialising the application, include Flask Blueprints for `auth`, `blogging` and `account`
- `helpers.py`: For [helper functions](https://www.geeksforgeeks.org/what-are-the-helper-functions/) that are used across the whole project, including setting certain pages as visible only if the user has logged in, and displaying apology messages
- `auth.py`: For creating and logging in user account
- `blogging.py`: For creating, editing, deleting and displaying blog posts
- `account.py`: For changing username and password
- `info.py`: For information about CS50 Flask Blog

In addition, the `blog/` folder contins the following subfolders:
- `database/`: Includes the `blog.db` SQL database file used for the entire application, storing data for user account and blog posts
- `static/`: For static files for the project, including CSS, favicon and asset files
- `templates/`: Page templates for the application, divided for different components:
    - `layout.html`: Base layout for the entire application, including the navigation bar (`_navbar.html`) and footer (`_footer.html`) components
    - `apology.html`: Page for displaying apology messages
    - `auth/` subfolder: Pages for user account registration (`register.html`) and user log-in (`login.html`).
    - `blogging/` subfolder: Pages for the home page (`index.html`), blog post creation (`create.html`), blog post editing and deletion (`edit.html`) and displaying posts (`_postlist.html`)
    - `account/` subfolder: Page for changing username and password (`account.html`)

## References
- [Build a Scalable Flask Web Project From Scratch](https://realpython.com/flask-project/) by Philipp Acsany
- [Building a Flask Blog: A Step-by-Step Guide for Beginners](https://medium.com/@noransaber685/building-a-flask-blog-a-step-by-step-guide-for-beginners-8bffe925cd0e) by Noran Saber Abdelfattah







Author : MAINAK SIL.
CITY: CHUNCURA, W-B, INDIA
GITHUB USERNAME:- MainakSil
EDX USERNAME:- Mainak_Sil
DATE: 24th MAY 2024.
