import picamera
import time
from datetime import datetime

class CameraCapture:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)

    def capture_image(self):
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
            img_path = f'images/{timestamp}.jpg'
            
            self.camera.start_preview()
            # Allow time for camera to adjust
            time.sleep(2)
            
            self.camera.capture(img_path)
            print(f"Image saved as {img_path}")
        finally:
            self.camera.stop_preview()

if __name__ == "__main__":
    capture = CameraCapture()
    capture.capture_image()
