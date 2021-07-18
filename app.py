import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(import_name=__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(func):
    """This function ensures blocking users from the backend
    by redirecting the user to the login page if the url would
    be copied and pasted in another browser or (icognito)tab, meaning
    that the user would not be in that session.
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function


@app.errorhandler(404)
def page_not_found(e):
    """If there is a 404 error in the app, this function
    returns the created 404.html file specified for 404 errors.
    """
    print(e)
    return render_template('404.html', e=e), 404


@app.route("/")
@app.route("/terms")
def terms():
    """ Finds all terms from the mongo database
    and displays them as a list on the terms.html template
    """

    all_terms = list(mongo.db.terms.find().sort("term_name", 1))
    return render_template("terms.html", terms=all_terms)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Searches for the text inserted in the form search bar in
    the mongo database and displays it on the terms.hmtl template/page.
    """
    dicty = {'CS': {'name': 'Cyber Security',
                    'template': 'cyber_security.html'},
             'DA': {'name': 'Data Analytics',
                    'template': 'data_analytics.html'},
             'WD': {'name': 'Web Development',
                    'template': 'web_development.html'}}

    to_search = request.args.get("search", "name").lower()
    if to_search == dicty.keys():
        response = "{}".format(to_search)
        return response

    query = request.args.get("query")
    all_terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
    return render_template("terms.html", terms=all_terms)


def search_by_field():
    """Search by field name and be redirected
    to that page.
    """
    field = {}  # query params url flask
    field_details = dict.get(field)
    list(mongo.db.terms.find({"field_name": field_details.name}))
    return render_template(field_details.template)


@app.route("/cyber_security")
def cyber_security():
    """ Finds all terms that have the Cyber Security field name and
    display them on the Cyber Security template/page.
    """
    all_terms = list(mongo.db.terms.find(
        {"field_name": "Cyber Security"}).sort("term_name", 1))
    return render_template("cyber_security.html", terms=all_terms)


@app.route("/data_analytics")
def data_analytics():
    """ Finds all terms that have the Data Analytics field name and
    display them on the Data Analytics template/page.
    """
    all_terms = list(mongo.db.terms.find(
        {"field_name": "Data Analytics"}).sort("term_name", 1))
    return render_template("data_analytics.html", terms=all_terms)


@app.route("/web_development")
def web_development():
    """ Finds all terms that have the Web Development field name and
    display them on the Web Development template/page.
    """
    all_terms = list(mongo.db.terms.find(
        {"field_name": "Web Development"}).sort("term_name", 1))
    return render_template("web_development.html", terms=all_terms)


@app.route("/register", methods=["GET", "POST"])
def register():
    """If the method is post, to register, inserting info via the form,
    the first check is if the username already exists in the database.
    If so, a message appears and the user is redirected to the register
    page to try again.
    Otherwise, the user's info, username and password,
    is inserted into the database, a message appears and the user is
    redirected to their own profile page.
    If the method is get, the register template/page displays.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        registered = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registered)

        session["user"] = request.form.get("username").lower()
        flash("Successful Registration!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """If the method is post, to login, first the check if the username
    already exists in the database. If it does, the check is if
    the entered password matches the username. If it does,
    redirects the user to their own profile page.
    If they do not match, or the username does not exist,
    a message appears and the user is redirected to the login page.
    If the method is get, the login template/page displays.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))

            # invalid password match
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        # username doesn't exist
        flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ To get the profile page, first the session
    user's username is retrieved from the database.
    Then, a list is created which finds the terms created by
    the session user, which is set equal to the username and
    terms display on the profile template/page.
    """
    # get the session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    all_terms = list(mongo.db.terms.find(
        {"created_by": session['user']}).sort("term_name", 1))
    return render_template("profile.html", username=username, terms=all_terms)


@app.route("/add_term", methods=["GET", "POST"])
@login_required
def add_term():
    """ If the request is post, to add a term, four
    different fields, three via the form and one is the
    logged in user, are inserted as a dictionary into the
    database. A message appears and the user is redirected
    to the terms page where all terms are displayed.
    Otherwise, all terms are displayed on the add term
    template/page in order of field name.
    """
    if request.method == "POST":
        term = {
            "field_name": request.form.get("field_name"),
            "term_name": request.form.get("term_name"),
            "term_definition": request.form.get("term_definition"),
            "created_by": session["user"]
        }
        mongo.db.terms.insert_one(term)
        flash("Term Successfully Added")
        return redirect(url_for("terms"))

    fields = mongo.db.fields.find().sort("field_name", 1)
    return render_template("add_term.html", fields=fields)


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
@login_required
def edit_term(term_id):
    """
    If the request method is post, to edit a term, a dictionary with
    three fields from the form and the user logged in, updates the
    corresponding id in the database and a message appears.
    Otherwise,
    """
    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    if not term or term['created_by'] != session['user']:
        return render_template("404.html")

    if request.method == "POST":
        submit = {
            "field_name": request.form.get("field_name"),
            "term_name": request.form.get("term_name"),
            "term_definition": request.form.get("term_definition"),
            "created_by": session["user"]
        }
        mongo.db.terms.update({"_id": ObjectId(term_id)}, submit)
        flash("Term Successfully Updated")

    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    fields = mongo.db.fields.find().sort("field_name", 1)
    return render_template("edit_term.html", term=term, fields=fields)


@app.route("/delete_term/<term_id>")
@login_required
def delete_term(term_id):
    """ Removes the id from the database that corresponds
    with term id from the url. Then, a message appears and
    the user is redirected to the terms template/page.
    """
    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    if not term:
        flash("Term already deleted")
        return redirect(url_for("terms"))

    if term['created_by'] != session['user']:
        return render_template("404.html")

    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    flash("Term Successfully Deleted")
    return redirect(url_for("terms"))


@app.route("/logout")
def logout():
    """A message, then the user is removed from session
    cookies and redirected to the login page.
    """
    # remove user from session cookies
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
