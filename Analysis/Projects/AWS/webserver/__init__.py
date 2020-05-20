from flask import Flask

webserver = Flask(__name__)

from webserver import routes

