#
from flask import Flask, render_template,url_for,redirect
# from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from flask_mysqldb import MySQL
# import mysql.connector
#
app = Flask(__name__)
Bootstrap(app)
# mydb= mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='12345678',
#     database='flaskapp'
# )
# my_cursor= mydb.cursor()
#
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='12345678'
# app.config['MYSQL_DB']='flaskapp'
@app.route('/')
def index():
    # return render_template('index.html')
    colors=['Red','Blue','Yellow']
    return render_template('index.html',colors=colors)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/css')
def css():
    return render_template('css.html')
@app.route('/dog')
def dog():
    return render_template('dog.html')
@app.route('/fox')
def fox():
    return render_template('fox.html')
@app.route('/croc')
def croc():
    return render_template('croc.html')


# def set():
#     name = 'lovely'
#     email = 'crocodile'
#     my_cursor.execute("INSERT INTO users(name,email) VALUES (%s, %s)",(name,email))
#     mydb.commit()
#
# def get():
#
#
#     my_cursor.execute("SELECT * FROM users")
#
#     myresult = my_cursor.fetchall()
#
#     for x in myresult:
#         print(x)







if __name__ == '__main__':
    # set()
    # get()
    app.run(debug= True)
