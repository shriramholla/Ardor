import cv2
import threading
from google.cloud import vision
import io

client = vision.ImageAnnotatorClient()
data = [0,0,0,0]
count = [0]
ratio = [0]

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        img = self.frame
        ret, jpeg = cv2.imencode('.jpg', img)
        edited = jpeg.tobytes()
        image = vision.types.Image(content=edited)
        response = client.face_detection(image=image)
        faces = response.face_annotations
        likelihood_name = (0, 0, 1, 1, 2, 3)
        people = len(faces)
        for face in faces:
            anger = likelihood_name[face.anger_likelihood]
            joy = likelihood_name[face.joy_likelihood]
            surprise = likelihood_name[face.surprise_likelihood]
            sorrow = likelihood_name[face.sorrow_likelihood]
            count[0] += 1
            data[0] += anger
            data[1] += joy
            data[2] += surprise
            data[3] += sorrow
            print(count[0])

            print("ANGER: {}\n".format(data[0]))
            print("JOY: {}\n".format(data[1]))
            print("SURPRISE: {}\n".format(data[2]))
            print("SORROW: {}\n".format(data[3]))
            express = sum(data)
            ratio[0] = express / (3 * count[0])
            print("Percentage = {}".format(ratio[0]*200))

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        
        return edited

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def stats():
    if count[0] == 0: count[0] = 1
    joy = data[1] * 200 / count[0]
    if joy > 100:
       joy = 100
    info = {'likeness': round(ratio[0] * 200, 2),
            'anger': round(data[0] * 200 / count[0], 2),
            'joy': round(joy, 2),
            'surprise': round(data[2] * 200 / count[0], 2),
            'sorrow': round(data[3] * 200 / count[0], 2),}
    return info

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')