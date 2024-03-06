from DHT11 import DHT11Sensor
from Camera import Camera

if __name__ == "__main__":
    capture = Camera()
    capture.capture_image()
      
      
    dht10 = DHT11Sensor(6) 
     
    humidity, temperature = dht10.dhtsensor.read_data()
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.0f}°C  Humidity: {humidity:.1f}%")
    else:
        print("Failed to retrieve data from sensor")
    
    dht10.dhtsensor.cleanup()

