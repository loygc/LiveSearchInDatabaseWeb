"""
 @Project: LiveSearchInDatabaseWeb
 @Author: loyio
 @Date: 6/10/21
"""
from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# Enter here your database informations

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123456',
                       database='python_quiz_db',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/livesearch", methods=["POST", "GET"])
def livesearch():
    searchtext = request.form.get("text")
    cursor = conn.cursor()
    sql = "select * from MultipleChoiceQuestion where QQuestion LIKE '%"+searchtext+"%' order by QNo"
    try:
        res = [int(cursor.execute(sql))]
        if res[0] == 0:
            res.append("error")
        else:
            res.append(cursor.fetchall())
    except Exception as e:
            res = [0, "error"]
    print(res[1])
    return jsonify(res[1])


if __name__ == "__main__":
    app.run(debug=True)
