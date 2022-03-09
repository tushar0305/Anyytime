from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import Response,send_file

app = Flask(__name__)

import rds_mysql as db

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/subscribe", methods=['POST'])
def subscribe():
    email_id = request.form['sub']

    if request.method == 'POST':
        email = request.form['sub']
        db.insert_details(email)
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
