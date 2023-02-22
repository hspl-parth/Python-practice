from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import psycopg2
from flask import request, url_for, redirect

# from flask_login import UserMixin
# from flask_wtf import FlaskFrom
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='parth',
                            password='password')
    return conn

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'

# db = SQLAlchemy(main)


# class hospital_patients(db.Model):
#     """docstring for hospital_patients"""
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     date_created = db.Column(db.DateTime, deafult=datetime.now)

#     def __repr__(self):
#         return '<name %r>' % self.id


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        First_name = request.form['First_name']
        Last_name = request.form['Last_name']
        Age = int(request.form['Age'])
        Address = request.form['Address']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO patients (First_name, Last_name, Age, Address)'
                    'VALUES (%s, %s, %s, %s)',
                    (First_name, Last_name, Age, Address))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM patients;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    print(books)
    return render_template('patient_index.html', books=books)

@app.route('/hospital/patients')
def hospital_patients():
    return render_template('index.html')


@app.route('/login')
def login_hospital():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM hospital_user;')
    h_users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('login.html', h_users=h_users)


@app.route('/register', methods=('GET', 'POST'))
def register_hospital():
    if request.method == 'POST':
        Name = request.form['Name']
        Login = request.form['Login']
        Password = request.form['Password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO hospital_user (Name, Login, Password)'
                    'VALUES (%s, %s, %s)',
                    (Name, Login, Password))
        conn.commit()
        cur.close()
        conn.close()


    return render_template('register.html')


# conn = sqlite3.connect('hospital_patients')

if __name__ == '__main__':
    app.run(debug=True)

