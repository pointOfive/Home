from flask import Flask
from flask import render_template, request

app = Flask(__name__)



@app.route('/welcome', methods = ['GET','POST'])
def welcome():
    name = request.form.get('name')
    return render_template('welcome.html', name = name)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
