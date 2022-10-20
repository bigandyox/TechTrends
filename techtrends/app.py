import sqlite3
import logging
import sys

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# Define global variables
global db_connection_count
db_connection_count = 0

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Function to get a database connection.
def get_db_connection():
    '''This function connects to database with the name database.db.'''
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the main route of the web application 
@app.route('/')
def index():
    global db_connection_count
    db_connection_count += 1
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define the healthcheck route of the web application 
@app.route('/healthz')
def healthcheck():
    try:
        connection = get_db_connection()
        connection.execute('SELECT * FROM posts').fetchall()
        connection.close()
        response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
        )
    except: 
        response = app.response_class(
            response=json.dumps({"result":"ERROR - unhealthy"}),
            status=500,
            mimetype='application/json'
        )
    return response

# Define the metrics route of the web application 
@app.route('/metrics')
def metrics():
    global db_connection_count
    db_connection_count += 1
    connection = sqlite3.connect('database.db')
    posts = connection.execute('SELECT * FROM posts').fetchall()
    post_count = len(posts)
    response = app.response_class(
            response=json.dumps({"db_connection_count": db_connection_count, "post_count": post_count}),
            status=200,
            mimetype='application/json'
    )
    return response

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      global db_connection_count
      db_connection_count += 1
      app.logger.info('Non-existing article')
      return render_template('404.html'), 404
    else:
      #global db_connection_count
      db_connection_count += 1
      app.logger.info('Article "{}" retrieved'.format(post['title']))
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.info('"About Us" page retrieved')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            global db_connection_count
            db_connection_count += 1
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            app.logger.info('Article "{}" created'.format(title))
            connection.close()

            return redirect(url_for('index'))

    return render_template('create.html')

# start the application on port 3111
if __name__ == "__main__":
# Stream logs to a file
   logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG, stream=sys.stdout)
   app.run(host='0.0.0.0', port='3111')