from flask import Flask 

app = Flask(__name__) 

@app.route('/post/<int:id>')    # convert string to integer
def show_post(id): 
	# Shows the post with given id. 
	return f'This post has the id {id}'

if __name__ == "__main__": 
	app.run(debug=True)