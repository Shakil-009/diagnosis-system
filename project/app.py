from flask import Flask, request, render_template
import mysql.connector

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	database = 'data',
	password = ''
)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/doctor')
def doctor():
    return "Welcome to the Doctor page!"

@app.route('/diagnosis')
def diagnosis():
    return render_template('diagnosis.html')


@app.route('/about')
def about():
    return "Welcome to the about page!"


@app.route('/contact')
def contact():
    return "Welcome to the contact page!"

@app.route('/a')
def a():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "a%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/b')
def b():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "b%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/c')
def c():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "c%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/d')
def d():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "d%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/e')
def e():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "e%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/f')
def f():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "f%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/g')
def g():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "g%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/h')
def h():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "h%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/i')
def i():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "i%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/j')
def j():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "j%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/k')
def k():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "k%"')
	results = cursor.fetchall()
	print (results)
	print (type(results))
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/l')
def l():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "l%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/m')
def m():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "m%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/n')
def n():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "n%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/o')
def o():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "o%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/p')
def p():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "p%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/q')
def q():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "q%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/r')
def r():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "r%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/s')
def s():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "s%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/t')
def t():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "t%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/u')
def u():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "u%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/v')
def v():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "v%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/w')
def w():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "w%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/x')
def x():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "x%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/y')
def y():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "y%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()

@app.route('/z')
def z():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM data WHERE LOWER(name) LIKE "z%"')
	results = cursor.fetchall()
	return render_template('all.html', results=results)
	cursor.close()
