from flask import Flask, render_template, Response, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('deployindex.html')

@app.route('/old')
def old():
    return render_template('deployold.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
