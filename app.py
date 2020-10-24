# https://blog.miguelgrinberg.com/post/video-streaming-with-flask
#https://flask.palletsprojects.com/en/1.1.x/quickstart/
# https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/


from flask import Flask, render_template, Response, url_for
from pi_models.pi_camera import Camera
from pi_models.temp_humid_sensor import getTempHum
from pi_models.pi_cpu_temp import getCpuTemp
from pi_models.pi_LED import change_led_state #,LED_on, LED_off

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    temp_humidity = getTempHum()    # Get it from sensor once per load
    cpu_temp = getCpuTemp()

    return render_template('index.html', temperature=temp_humidity[0], humidity=temp_humidity[1], cpu_temp=cpu_temp) # Pass parameters here  # Pass video object here.

# Should this be abstracted away??
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# User can go to /video_feed for stream, or just look at main page.
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/old')
def old():
    return render_template('old.html')

@app.route('/<state>/<pin>')
def LED_state(state, pin):

    state = int(state)
    pin = int(pin)
    change_led_state(state,pin)

    return f"led {pin} changed to {state}"

@app.route("/who")
def hello():
    return "Created by David Saunders"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
