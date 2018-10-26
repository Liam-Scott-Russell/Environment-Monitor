from flask import Flask
import flask
import Adafruit_DHT

app = Flask(__name__)


# routing for the pages of the web app
@app.route("/")
@app.route("/monitor")

def monitor():
    """Returns the values for temperature and humidity"""

    # GPIO pin to which the data cable of the sensor is connected
    pin = 14

    # selects the type of sensor from the available ones in the package
    sensor = Adafruit_DHT.DHT22

    # retrieves the raw data for temperature and humidity
    # uses read_retry so that it retries the measurements occasionly
    rawHumidity, rawTemperature = Adafruit_DHT.read_retry(sensor, pin)

    # formats the temperature and humidity to display properly
    temperature = 'Temperature: {:0.1f}*'.format(rawTemperature)
    humidity = 'Humidity: {:0.1f}%'.format(rawHumidity)

    # creates the HTML response for a GET request
    response = flask.Response(temperature + "\n" + humidity + "\n")
    # necessary so that the text displays properly
    response.headers["Content-type"] = 'text/plain'
    return response


if __name__ == '__main__':
    # run the app on localhost:5000 (5000 is default port)
    app.run(host='0.0.0.0')
