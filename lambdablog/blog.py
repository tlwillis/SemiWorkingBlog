from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('food.html')

@app.route('/enternew')
def enternew():
	return render_template('food.html')

@app.route('/addfood', methods=['POST'])
def addfood():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	try:
		name = request.form['name']
		calories = request.form['calories']
		cuisine = request.form['cuisine']
		is_vegetarian = request.form['is_vegetarian']
		is_gluten_free = request.form['is_gluten_free']

		cursor.execute('INSERT INTO food (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name,calories,cuisine,is_vegetarian,is_gluten_free))
		connection.commit()
		message = 'Post Successful'
	except:
		connection.rollback()
		message = 'Error shit'
	finally:
		return render_template('result.html', message=message)
		connection.close()