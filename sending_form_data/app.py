'''
A Form in HTML is used to collect the information of required entries which are then 
forwarded and stored on the server. These can be requested to read or modify the form. 
The Python with flask provides this facility by using the URL rule. In the given 
example below, the ‘/’ URL renders a web page(student.html) which has a form. 
The data filled in it is posted to the ‘/result’ URL which triggers the result() function. 
The results() function collects form data present in request.form in 
a dictionary object and sends it for rendering to result.html.
'''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)