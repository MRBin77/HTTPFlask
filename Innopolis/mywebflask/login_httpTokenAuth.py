from flask import Flask, render_template, request, g, jsonify, redirect, url_for
from flask_httpauth import HTTPTokenAuth
import os

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')


tokens = {
    os.environ.get('MYPASS', '1234'): "User1"
}


@app.route('/')
def login():
    return render_template('login.html')


@auth.verify_token
def verify_token(token):
    #token = request.form.get('password')
    if token in tokens:
        return tokens[token]



@app.route('/login', methods=['POST'])
def login_post():
    #login = request.form.get('login')
    login = verify_token(request.form.get('password'))
    return redirect(url_for('index'))



@app.route('/')
@auth.login_required
def index():
    #email = request.form.get('email')
   #password = request.form.get('password')
    #return jsonify({"USERNAME": auth.current_user()})
    return "Hello, {}!".format(auth.current_user())



if __name__ == '__main__':
    app.run(debug=True)

