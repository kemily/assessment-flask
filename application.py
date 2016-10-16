from flask import Flask, render_template, request, session, flash
import jinja2
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Return homepage"""

    return render_template("index.html")

@app.route("/application-form")
def form_page():
    """Return application form page"""

    return render_template("application-form.html")

@app.route("/application", methods=['POST'])
def application_response():
    """Returns responce from the form page in a form of a message"""

    #getting first and last name, salary, job title from the user input form
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    title = request.form.get("job")
    salary = request.form.get("salary")

    #assigning first and last name of the user to a current_user variable
    current_user = first_name + " " + last_name

    #creating a session of current user, assigning a dictionary with
    #the input infromation of the user.
    session[current_user] = {"first_name": first_name,
                             "last_name": last_name,
                             "title": title,
                             "salary": salary}

    flash("Thank you, %s! Your input is added!" % (first_name))

    #once the form is submitted the user is redirected to the application
    #response page, with the input info.
    return render_template("application-response.html",
                            first_name=first_name,
                            last_name=last_name,
                            title=title,
                            salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
