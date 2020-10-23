import time
import cv2

# camera_port = 0
# camera = cv2.VideoCapture(camera_port)
# #time.sleep(0.1)  # If you don't wait, the image will be dark
# return_value, image = camera.read()
# cv2.imwrite("opencv.png", image)
# del(camera)  # so that others can use the camera as soon as possible


# class Camera(object):
#     """An emulated camera implementation that streams a repeated sequence of
#     files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    
#     def __init__(self):
#         self.camera_port = 0

#     def get_frame(self):

#         camera = cv2.VideoCapture(self.camera_port) # Takes picture

#         return_value, image = camera.read() # return_value = true if image taking was successful

#         return image

class Camera(object):
    def init(self):
        # self.video = cv2.VideoCapture('video.mp4')
        self.video = cv2.VideoCapture(0)


def __del__(self):
    self.video.release()

def get_frame(self):
    success, image = self.video.read()
    ret, jpeg = cv2.imencode('.jpg', image) # Encode to JPEG
    return jpeg.tobytes()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# gen(Camera())