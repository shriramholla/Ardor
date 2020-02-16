import io
import os
import cv2
import time
import keyboard


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def camera():
	print("Hello")

# data = [0,0,0,0]
# count = [0]
# key = [0]
# def breakloop():
#     key[0] = 1
# def detect_faces(path, img):
#     """Detects faces in an image."""
#     from google.cloud import vision
#     import io
#     client = vision.ImageAnnotatorClient()

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.face_detection(image=image)
#     faces = response.face_annotations

#     # Names of likelihood from google.cloud.vision.enums
#     likelihood_name = (0, 0, 1, 2, 3, 4)
#     print('Faces:')
#     people = len(faces)
#     for face in faces:
#         anger = likelihood_name[face.anger_likelihood]
#         joy = likelihood_name[face.joy_likelihood]
#         surprise = likelihood_name[face.surprise_likelihood]
#         sorrow = likelihood_name[face.sorrow_likelihood]
#         count[0] += 1
#         vertices=[]
#         for vertex in face.bounding_poly.vertices:
#             vertices.append((vertex.x, vertex.y))

#         print(vertices[0])
#         print(vertices[-2])

#         data[0] += anger
#         data[1] += joy
#         data[2] += surprise
#         data[3] += sorrow


#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))


# def show_webcam(mirror=False):
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret_val, img = cam.read()
#         if mirror:
#             img = cv2.flip(img, 1)

#         cv2.imwrite('mango.jpg', img)
#         detect_faces('mango.jpg', img)
#         if(key[0] == 1):
#             break
#     cv2.destroyAllWindows()
#     emotions = ((data[1] * 1.25 + data[2] * 0.75 + data[0] * 0.5 + data[3])/(4 * count)) * 100
#     print("Percentage = {}".format(emotions))
#     print("ANGER: {}\n".format(data[0]))
#     print("JOY: {}\n".format(data[1]))
#     print("SURPRISE: {}\n".format(data[2]))
#     print("SORROW: {}\n".format(data[3]))

