import board
from lcd import drivers
import adafruit_dht
import time

# Initialize LCD display
display = drivers.Lcd()

# Define the sensor type (DHT11) and pin
DHT_SENSOR = adafruit_dht.DHT11(board.D4)

try:
    while True:
        # Read sensor values
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity

        if humidity is not None and temperature is not None:
            print("Temperature: {:.1f}°C".format(temperature))
            print("Humidity: {:.1f}%".format(humidity))
            # Clear the display
            display.lcd_clear()
            # Display temperature and humidity on LCD
            display.lcd_display_string("Temp: {:.1f}C".format(temperature), 1)
            display.lcd_display_string("Humidity: {:.1f}%".format(humidity), 2)
        else:
            print("Failed to retrieve data from sensor. Check wiring and retry.")

        # Delay for one minute
        time.sleep(60)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
    display.lcd_backlight(0)
except RuntimeError as error:
    print("Error reading data from DHT sensor:", error)
finally:
    print("Cleaning up!")
    display.lcd_clear()
    display.lcd_backlight(0)



