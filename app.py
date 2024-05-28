from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "asdfghjkl"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True, unique=True)
    name = db.Column("name", db.String(100), nullable=False)
    email = db.Column("email", db.String(100), nullable=False, unique=True)

# insert other necessary parameters

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    # insert session code block here
    return render_template('home.html')

@app.route("/dashboard")
def dashboard():
    # insert session code block here
    return render_template('index.html')

@app.route("/contact-us")
def contact():
    # insert session code block here
    return render_template('contact-us.html')

@app.route("/about-us")
def about():
    # insert session code block here
    return render_template('about.html')

@app.route("/announcements")
def announcement():
    # insert session code block here
    return render_template('announcements.html')

@app.route("/programs-and-events")
def prog_and_events():
    # insert session code block here
    return render_template('events.html')

# insert logout route here
# @app.route("/logout")
# def logout():
    # remove comment and insert other necessary session parameters
#    session.pop("user", None)
#    return redirect(url_for('login'))

if __name__ == '__main__':
#    db.create_all()
    app.run(debug=True)