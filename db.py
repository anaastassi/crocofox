# from flask_mysqldb import MySQL
# import mysql.connector
#
#
# def init():
#     mydb = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         passwd='12345678',
#         database='flaskapp'
#     )
#
#     return  mydb
#
# def set(db,name,data):
#
#     db.cursor().execute("INSERT INTO users(name,email) VALUES (%s, %s)",(name,data))
#     db.commit()
#
# def get(db, nameForItemWhatIFind):
#
#
#     cursor=db.cursor()
#     cursor.execute("SELECT * FROM users where name='" +nameForItemWhatIFind+"'")
#
#     myresult = cursor.fetchall()
#
#     for x in myresult:
#         return x
#     #     if x.. == "data":
#     #         return x/..
#
