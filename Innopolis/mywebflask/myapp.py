from flask import Flask, render_template, url_for
from jinja2 import Template

app = Flask(__name__)

# @app.route('/')
# def index():
#     # template = Template('login.html')
#     # return render_template('login.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)