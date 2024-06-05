from flask import Flask
app = Flask(__name__)   # Flask constructor

@app.route('/')
def run_me():
    return 'App started.'

# Decorator to route URL - then hello_world() will be called.
@app.route('/hello') 

# Binding to the function of route.
def hello_world():
    return 'hello world'

# The add_url_rule() function of an application object can also be used to bind URL with a function.
app.add_url_rule('/helloworld', 'helloworld', hello_world)

# The gfg function is now mapped with the “/g2g” path.
def gfg():
   return 'geeksforgeeks'
app.add_url_rule('/g2g', 'gfg', gfg)

# Routing the decorator function hello_name with a variable.
''' The parameter of route() decorator contains the variable part attached to the URL '/hello' as an argument. '''
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/user/<username>') 
def show_user(username): 
    # Greet the user 
    return f'Hello {username} !'

# http://localhost:5000/blog/1
@app.route('/blog/<postID>') 
def show_blog(postID): 
    postID = float(postID)  # convert string to float
    return 'Blog Number %d' % postID 

# http://localhost:5000/rev/1.1
@app.route('/rev/<revNo>') 
def revision(revNo):
    revNo = float(revNo)  # convert string to float
    return 'Revision Number %f' % revNo 


if __name__=='__main__':
    app.debug = True
    app.run()
    #app.run(debug = True)  # alternate