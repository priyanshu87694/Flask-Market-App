from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Change Text'

@app.route('/about')
def about_page():
    return "<h1>This is about page</h1>"