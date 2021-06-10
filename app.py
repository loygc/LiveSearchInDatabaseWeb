"""
 @Project: LiveSearchInDatabaseWeb
 @Author: loyio
 @Date: 6/10/21
"""
from flask import Flask,render_template,request,jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)

#Enter here your database informations
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123456"
app.config["MYSQL_DB"] = "python_quiz_db"
app.config["MYSQL_CURSORCLASS"] = ""

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "select * from MultipleChoiceQuestion where QQuestion LIKE '%{}%' order by QNo".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)