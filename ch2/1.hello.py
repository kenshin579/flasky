from flask import Flask

# initialization
app = Flask(__name__)

# routes and function views
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!<h1>' % name

# server startup
if __name__ == '__main__':
    app.run(debug=True)
