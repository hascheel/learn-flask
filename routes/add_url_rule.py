'''
The add_url_rule() function – The URL mapping can also be done using the 
add_url_rule() function. This approach is mainly used in case we are 
importing the view function from another module. In fact, the app.route calls 
this function internally.

Syntax: add_url_rule(<url rule>, <endpoint>, <view function>)

'''
# Example: In the below example, we will try to map the show_user view function using this approach.
from flask import Flask 

app = Flask(__name__) 

def show_user(username): 
	# Greet the user 
	return f'Hello {username} !'
	
app.add_url_rule('/user/<username>', 'show_user', show_user) 

if __name__ == "__main__": 
	app.run(debug=True)