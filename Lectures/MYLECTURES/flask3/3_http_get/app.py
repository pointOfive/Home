from flask import Flask
from flask import render_template, request

app = Flask(__name__)


#@app.route('/<name>')
@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('index.html', name = name)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
