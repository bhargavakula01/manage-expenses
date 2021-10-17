#from firebase import firebase
from flask import Flask, render_template, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/home')
def index():
    return {'file_run' : True}



if __name__ == "__main__":
    app.run()