from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def index ():

    name = 'Anderson Angulo'

    return render_template('index.html', name = name)