from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user       

#import datetime to change date format


@app.route("/")
def form():
    return render_template("create.html")

@app.route('/register', methods=["POST"])
def create_user():
    if not request.form:
        flash("Please register", "register")
        return redirect("/")
    if not user.User.validate_user(request.form):
        # we redirect to the template with the form.
            return redirect('/')
    # We pass the data dictionary into the save method from the User class.
    id= user.User.save(request.form)

    # Don't forget to redirect after saving to the database.
    return redirect('/wall')            

@app.route("/wall")
def read():

    users = user.User.get_all_users()

    return render_template("wall.html", users=users)

