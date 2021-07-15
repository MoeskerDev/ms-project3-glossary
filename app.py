import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/terms")
def terms():
    terms = list(mongo.db.terms.find())
    return render_template("terms.html", terms=terms)


@app.route("/cyber_security")
def cyber_security():
    cyber = list(mongo.db.fields.find())
    return render_template("cyber_security.html", cyber=cyber)


@app.route("/data_analytics")
def data_analytics():
    fields = mongo.db.fields.find()
    return render_template("data_analytics.html", fields=fields)


@app.route("/web_development")
def web_development():
    fields = mongo.db.fields.find()
    return render_template("web_development.html", fields=fields)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Successful Registration!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
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
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_term", methods=["GET", "POST"])
def add_term():
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
def edit_term(term_id):
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
def delete_term(term_id):
    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    flash("Term Successfully Deleted")
    return redirect(url_for("terms"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
