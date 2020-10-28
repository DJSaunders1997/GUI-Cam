from flask import Flask, render_template, Response, url_for
import requests

app = Flask(__name__)
piIP = 'http://192.168.68.135:5000' # Needs the http so requests knows how to connect


@app.route('/')
@app.route('/index')
def index():
    return render_template('deployindex.html')

@app.route('/old')
def old():
    return render_template('deployold.html')

#turn on green LED
@app.route('/toggle_red_led')
def toggle_red_led():
    x = requests.get(f'{piIP}/toggle_red_led')
    return (x)

#turn on red LED
@app.route('/toggle_green_led')
def toggle_green_led():
    x = requests.get(f'{piIP}/toggle_green_led')
    return (x)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
