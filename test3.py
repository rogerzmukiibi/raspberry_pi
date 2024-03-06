import board
import adafruit_dht
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

class ParameterCapture:
    def __init__(self):
        self.HIVEID = "your_hive_id_here"  # Replace with your actual hive ID
        self.filename = f"/home/pi/Desktop/HiveMonitor2/parameter_capture/sensor_data/{self.HIVEID}.csv"

        # Initialize DHT22 sensor
        self.dht22 = adafruit_dht.DHT22(board.D5)

        # Initialize LCD
        self.lcd_columns = 16
        self.lcd_rows = 2
        self.i2c = board.I2C()
        self.lcd = character_lcd.Character_LCD_RGB_I2C(self.i2c, self.lcd_columns, self.lcd_rows)

    def measure_temperature_humidity(self):
        try:
            temperature = self.dht22.temperature
            humidity = self.dht22.humidity
        except Exception as e:
            print("Error with DHT22 sensor:", e)
            temperature = None
            humidity = None
        return temperature, humidity

    def display_on_lcd(self, temperature, humidity):
        if temperature is not None and humidity is not None:
            self.lcd.clear()
            self.lcd.message = f"Temp: {temperature:.1f}C\nHumidity: {humidity:.1f}%"
        else:
            self.lcd.clear()
            self.lcd.message = "Failed to read\nsensor data."

if __name__ == "__main__":
    param_capture = ParameterCapture()

    temperature, humidity = param_capture.measure_temperature_humidity()
    param_capture.display_on_lcd(temperature, humidity)
