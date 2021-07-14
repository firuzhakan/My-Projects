<<<<<<< HEAD
# Import Flask modules
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Create an object named app
app = Flask(__name__)

# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create users table within MySQL db and populate with sample data
# Execute the code below only once.
# Write sql code for initializing users table..
drop_table = 'DROP TABLE IF EXISTS users;'
users_table = """
=======
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# - configure required environmental variables for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# - drop users table if exists, create new users table and add some rows for sample
drop_table = 'DROP TABLE IF EXISTS users;'
users_table = """ 
>>>>>>> cde3d0bc7abbc685843e371c6cc866491a43c1f3
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""
data = """
INSERT INTO users
VALUES
<<<<<<< HEAD
	("Buddy Rich", "buddy@clarusway.com" ),
	("Candido", "candido@clarusway.com"),
	("Charlie Byrd", "charlie.byrd@clarusway.com");
"""

=======
	("Tuba", "tuba@amazon.com" ),
	("Ethan", "ethan@micrasoft.com"),
	("mostafa", "mostafa@facebook.com"),
    ("sait", "sait@tesla.com"),
    ("busra","busra@google");
"""


# - Execute sql commands and commit them
>>>>>>> cde3d0bc7abbc685843e371c6cc866491a43c1f3
db.session.execute(drop_table)
db.session.execute(users_table)
db.session.execute(data)
db.session.commit()

<<<<<<< HEAD
# Write a function named `find_emails` which find emails using keyword from the user table in the db,
# and returns result as tuples `(name, email)`.
=======
# - Write a function named `find_emails` which find emails using keyword from the user table in the db,
# - and returns result as tuples `(name, email)`.
>>>>>>> cde3d0bc7abbc685843e371c6cc866491a43c1f3
def find_emails(keyword):
    query = f"""
    SELECT * FROM users WHERE username like '%{keyword}%';
    """
    result = db.session.execute(query)
    user_emails = [(row[0], row[1]) for row in result]
<<<<<<< HEAD
    # if there is no user with given name in the db, then give warning
    if not any(user_emails):
        user_emails = [('Not found.', 'Not Found.')]
    return user_emails

# Write a function named `insert_email` which adds new email to users table the db.
def insert_email(name, email):
    query = f"""
    SELECT * FROM users WHERE username like '{name}';
    """
    result = db.session.execute(query)
    # default text
    response = 'Error occurred..'
    # if user input are None (null) give warning
    if name == None or email == None:
        response = 'Username or email can not be emtpy!!'
    # if there is no same user name in the db, then insert the new one
=======
    if not any(user_emails):
        user_emails = [("Not Found", "Not Found")]
    return user_emails


# - Write a function named `insert_email` which adds new email to users table the db.
def insert_email(name,email):
    query = f"""
    SELECT * FROM users WHERE username like '{name}'
    """
    result = db.session.execute(query)
    response = ''
    if len(name) == 0 or len(email) == 0:
        response = 'Username or email can not be empty!!'
>>>>>>> cde3d0bc7abbc685843e371c6cc866491a43c1f3
    elif not any(result):
        insert = f"""
        INSERT INTO users
        VALUES ('{name}', '{email}');
        """
        result = db.session.execute(insert)
        db.session.commit()
<<<<<<< HEAD
        response = f'User {name} added successfully'
    # if there is user with same name, then give warning
    else:
        response = f'User {name} already exits.'
    return response

# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')
@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':
        user_name = request.form['username']
        user_emails = find_emails(user_name)
        return render_template('emails.html', name_emails=user_emails, keyword=user_name, show_result=True)
    else:
        return render_template('emails.html', show_result=False)

# Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['useremail']
        result = insert_email(user_name, user_email)
        return render_template('add-email.html', result=result, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)

# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == '__main__':
    app.run(debug=True)
   #app.run(host='0.0.0.0', port=80)
=======
        response = f"User {name} and {email} have been added successfully"
    else:
        response = f"User {name} already exist"
    return response


# - Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# - using template files named `emails.html` given under `templates` folder
# - and assign to the static route of ('/')
@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':
        user_app_name = request.form['user_keyword']
        user_emails = find_emails(user_app_name)
        return render_template('emails.html', name_emails=user_emails, keyword=user_app_name, show_result=True)
    else:
        return render_template('emails.html', show_result=False)


# - Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# - using template files named `add-email.html` given under `templates` folder
# - and assign to the static route of ('/add')
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_app_name = request.form['username']
        user_app_email = request.form['useremail']
        result_app = insert_email(user_app_name, user_app_email)
        return render_template('add-email.html', result_html=result_app, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)


# - Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__=='__main__':
    app.run(debug=True)
>>>>>>> cde3d0bc7abbc685843e371c6cc866491a43c1f3
