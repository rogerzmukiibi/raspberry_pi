import board
import adafruit_dht

class ParameterCapture:
    def __init__(self):
        self.HIVEID = "your_hive_id_here"  # Replace with your actual hive ID
        self.filename = f"/home/pi/Desktop/HiveMonitor2/parameter_capture/sensor_data/{self.HIVEID}.csv"

        # Initialize DHT22 sensor
        self.dht22 = adafruit_dht.DHT22(board.D5)

    def measure_temperature_humidity(self):
        try:
            temperature = self.dht22.temperature
            humidity = self.dht22.humidity
        except Exception as e:
            print("Error with DHT22 sensor:", e)
            temperature = None
            humidity = None
        return temperature, humidity

if __name__ == "__main__":
    param_capture = ParameterCapture()

    temperature, humidity = param_capture.measure_temperature_humidity()
    if temperature is not None and humidity is not None:
        print("Temperature:", temperature)
        print("Humidity:", humidity)
    else:
        print("Failed to read temperature and humidity data.")
