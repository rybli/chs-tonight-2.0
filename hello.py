from flask import Flask
from flask import render_template

app = Flask(__name__,
            template_folder="templates")


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')
