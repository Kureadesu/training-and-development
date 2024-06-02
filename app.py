from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)
app.secret_key = "asdfghjkl"
app.permanent_session_lifetime = timedelta(minutes=5)

# Database connection function
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$4Y my n4m3",
            database="saad"
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Endpoint to update progress
@app.route('/update-progress', methods=['POST'])
def update_progress():
    data = request.get_json()
    user_id = data['user_id']
    module_name = data['module_name']
    progress = data['progress']
    
    connection = create_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO training_progress (user_id, module_name, progress)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE progress=%s, updated_at=NOW()
        """, (user_id, module_name, progress, progress))
        connection.commit()
        return jsonify({'success': True}), 200
    except Error as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()


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

@app.route("/training-and-development")
def training():
    # insert session code block here
    return render_template('training.html')

@app.route("/training-and-development/modules/leadership-training")
def leadership():
    # insert session code block here
    return render_template('module-1.html')

@app.route("/training-and-development/modules/community-engagement")
def community():
    # insert session code block here
    return render_template('module-2.html')

@app.route("/training-and-development/modules/basic-life-support")
def basic_life_support():
    return render_template('module-3.html')

# insert logout route here
# @app.route("/logout")
# def logout():
    # remove comment and insert other necessary session parameters
#    session.pop("user", None)
#    return redirect(url_for('login'))

if __name__ == '__main__':
#    db.create_all()
    app.run(debug=True)