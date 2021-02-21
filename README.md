# GUI-Cam
Raspberry pi webcam to monitor the crested gecko named GUI view at <s> www.guicam.eu .</s> Since leaving the EU that domain name no longer works, now use www.guicam.uk .

Web app created using python with the Flask library.
It was made pretty using Bootstrap css.
Was made dynamic using jQuery.
Domain name registered with Gandi and later GoDaddy and websited hosted on Heroku.
Video and LEDs controlled with a Raspberry pi 3B+, humidity recorded with a DHT22 sensor.

The app deploy.py is run on a server using Heroku.
THe app pi-app.py is run on raspberry pi on startup to stream video and handle LEDs.
