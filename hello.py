from flask import  Flask, render_template, url_for
from datetime import datetime
from markupsafe import escape

app = Flask(__name__)

#Filtro personalizados
@app.add_template_filter
def today (date):

    return date.strftime('%d-%m-%y')

#Funcion personalizada
@app.add_template_global
def repeat (s,n):

    return s * n

@app.route('/')
def index ():
    print (url_for('index'))
    print (url_for('data'))
    print (url_for('code', code = "Print()"))
    name = 'Anderson Angulo'
    friends = ["David", "Joe", "Adrian", "Daniel"]
    date = datetime.now()

    return render_template('index.html', name = name, friends = friends, date = date)

@app.route('/data')
@app.route('/data/<name>')
@app.route('/data/<name>/<int:age>')
@app.route('/data/<name>/<int:age>/<email>')
def data (name = None, age = None, email = None):

    my_data = {
        'name' : name,
        'age' : age,
        'email' : email 

    }

    return render_template('data.html', data = my_data)

@app.route('/code/<path:code>')
def code (code):
    code = escape(code) 
    return render_template("code.html", code= code)


@app.route('/login')
def login():

    return render_template("login.html")
    #Se recomienda dar saltos de lineas cuando son varios valores