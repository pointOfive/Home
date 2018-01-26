from flask import Flask
from flask import render_template, request

app = Flask(__name__)


#@app.route('/<name>')
@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html', title = "Flask -- Template Inheritance")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
