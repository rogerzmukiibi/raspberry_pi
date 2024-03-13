import board
from adafruit_character_lcd.character_lcd_rgb_i2c import Character_LCD_RGB_I2C
import adafruit_dht
import time

# Define the LCD size
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD
lcd = Character_LCD_RGB_I2C(board.I2C(), lcd_columns, lcd_rows)

# Define the sensor type (DHT11) and pin
dht_sensor = adafruit_dht.DHT11(board.D4)

try:
    while True:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        if humidity is not None and temperature is not None:
            lcd.clear()
            lcd.message = "Temp: {:.1f}C\nHumidity: {:.1f}%".format(temperature, humidity)
        else:
            lcd.clear()
            lcd.message = "Failed to read\nsensor data"
        time.sleep(2)  # Update every 2 seconds
except RuntimeError as error:
    print("Error reading data from DHT sensor:", error)
finally:
    lcd.clear()
    lcd.color = [0, 0, 0]  # Turn off the LCD backlight
