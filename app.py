#https://flask.palletsprojects.com/en/1.1.x/quickstart/
# https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html') # Pass parameters here  # Pass video object here.

@app.route("/who")
def hello():
    return "Created by David Saunders"



if __name__ == "__main__":
    app.run(host='0.0.0.0')