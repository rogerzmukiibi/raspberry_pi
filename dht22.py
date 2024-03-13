import board
import adafruit_dht

# Define the sensor type (DHT22) and pin
DHT_SENSOR = adafruit_dht.DHT11(board.D4)

try:
    temperature = DHT_SENSOR.temperature
    humidity = DHT_SENSOR.humidity
    if humidity is not None and temperature is not None:
        print("Temperature: {:.1f}°C".format(temperature))
        print("Humidity: {:.1f}%".format(humidity))
    else:
        print("Failed to retrieve data from sensor. Check wiring and retry.")
except RuntimeError as error:
    print("Error reading data from DHT sensor: {}".format(error))
