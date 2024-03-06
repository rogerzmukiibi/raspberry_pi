from picamera import PiCamera
import time
from datetime import datetime

timestring = datetime.now().strftime('%Y-%m-%d_%H%M%S')

class Capture:
    def __init__(self):
        self.camera = PiCamera()
    
    def init_camera(self):
        if self.camera is None:
            self.camera = PiCamera()
            self.camera.resolution = (640, 480)
        
        
        
        
        
        
        

    def capture_image(self):
        time.sleep(2)
        img_path = 'images/' + timestring + '.jpg'
        self.camera.start_preview()
        time.sleep(2)  # Allow time for camera to adjust
        self.camera.capture(img_path)
        self.camera.stop_preview()
        print(f"Image saved as {img_path}")

# Example usage
if __name__ == "__main__":
    capture = Capture()
    capture.capture_image()