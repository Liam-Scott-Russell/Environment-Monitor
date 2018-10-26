from flask import Flask
import Adafruit_DHT

app = Flask(__name__)
@app.route("/")

def readEnvironment():
	pin = 14
	sensor = Adafruit_DHT.DHT22
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return "Temperature: {:0.1f}*".format(temperature) + "\n" + "Humidity: {:0.1f}%".format(humidity)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
