import time
from picamera import PiCamera
from datetime import datetime
from lcd import drivers


timestring = datetime.now().strftime('%Y-%m-%d_%H%M%S')

class Camera:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)
        self.display = drivers.Lcd()

    def capture_image(self):
        img_path = 'images/' + timestring + '.jpg'
        self.camera.start_preview()
        time.sleep(2)  # Allow time for camera to adjust
        self.camera.capture(img_path)
        self.camera.stop_preview()
        print(f"Image saved as {img_path}")
        # Display message on LCD
        self.display_message("Image captured")

    def display_message(self, message):
        # Clear the display
        self.display.lcd_clear()
        # Display message on LCD
        self.display.lcd_display_string(message, 1)

if __name__ == "__main__":
    capture = Camera()
    capture.capture_image()
