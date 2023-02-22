import psycopg2
import os

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='parth',
        password='password')


cur = conn.cursor()

cur.execute('CREATE TABLE patients (id serial PRIMARY KEY,'
                                 'First_name varchar (150) NOT NULL,'
                                 'Last_name varchar (50) NOT NULL,'
                                 'Age integer NOT NULL,'
                                 'Address text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO patients (First_name, Last_name, Age, Address)'
            'VALUES (%s, %s, %s, %s)',
            ('Parth',
             'Vansjaliya',
             29,
             'Shilpan bliss')
            )

cur.execute('CREATE TABLE hospital_user (id serial PRIMARY KEY,'
                                'Name varchar (50) NOT NULL,'
                                'Login varchar (50) NOT NULL,'
                                'Password varchar (15) NOT NULL);'
                                )
conn.commit()

cur.close()
conn.close()