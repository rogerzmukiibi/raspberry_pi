import Adafruit_DHT
import RPi.GPIO


class DHT11Sensor:
    def __init__(self, sensor_pin, sensor_type=Adafruit_DHT.DHT11):
        """
        Initializes the DHT11 sensor object.

        Args:
            sensor_pin (int): The GPIO pin number connected to the sensor.
            sensor_type (optional): The type of DHT sensor (DHT11 or DHT22). Defaults to DHT11.
        """
        self.sensor_pin = sensor_pin
        self.sensor_type = sensor_type
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(self.sensor_pin, RPi.GPIO.OUT)

    def read_data(self):
        """
        Reads temperature and humidity data from the DHT11 sensor.

        Returns:
            tuple(float, float): A tuple containing temperature (Celsius) and humidity (%).
                Returns (None, None) if data retrieval fails.
        """
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor_type, self.sensor_pin)
            return humidity, temperature
        except Exception as e:
            print(f"Error reading from DHT11 sensor: {e}")
            return None, None

    def cleanup(self):
        """
        Cleans up GPIO resources after sensor usage.
        """
        RPi.GPIO.cleanup()
        
if __name__ == "__main__":
          
    dht11 = DHT11Sensor(5) 
     
    humidity, temperature = dht11.read_data()
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.0f}°C  Humidity: {humidity:.1f}%")
    else:
        print("Failed to retrieve data from sensor")
    
    dht11.cleanup()
