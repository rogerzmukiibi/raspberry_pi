import time
from picamera import PiCamera
from datetime import datetime

timestring = datetime.now().strftime('%Y-%m-%d_%H%M%S')

class Camera:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)

    def capture_image(self):
        img_path =  timestring + '.jpg'
        self.camera.start_preview()
        time.sleep(2)  # Allow time for camera to adjust
        self.camera.capture(img_path)
        self.camera.stop_preview()
        print(f"Image saved as {img_path}")
    
if __name__ == "__main__":
    capture = Camera()
    capture.capture_image()