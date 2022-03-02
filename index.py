from flask import Flask, render_template, request
from pymysql import connections

app = Flask(__name__)

db_conn = connections.Connection(
    host='anyytime.cbh9no9tsabi.us-east-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='abhay234',
    db='anyytime'

)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/index", methods=['POST'])
def AddEmail():
    email_id = request.form['sub']

    insert_sql = "INSERT INTO anyytime_data VALUES (%s)"
    cursor = db_conn.cursor()
    cursor.execute(insert_sql, (email_id))
    db_conn.commit()
    cursor.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
