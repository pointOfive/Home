from flask import Flask
from flask import render_template, request

app = Flask(__name__)


#@app.route('/<name>')
@app.route('/')
def index():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('index.html', first=first, last=last)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
