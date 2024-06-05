# Build a URL in Flask
''' Dynamic Building of the URL for a specific function is done using url_for() function. The function accepts the name of the function as first argument, and one or more keyword arguments. '''

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

# http://localhost:5000/user/admin
# http://localhost:5000/user/Horst

if __name__ == '__main__':
    app.run(debug=True)