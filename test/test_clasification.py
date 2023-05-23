#from keras.models import load_model  # TensorFlow is required for Keras to work
#import tensorflow.keras
import tensorflow 
import cv2  # Install opencv-python
#import keras 
import numpy as np
import os
from time import sleep

confidence_threshold = 0.9
piece = ""

# Load the model
model = tensorflow.keras.models.load_model("object_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:

   
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Change brightness and contrast of image
    image = cv2.addWeighted( image, 3., image, 0., 1.)
    
    # Show the image in a window
    cv2.imshow("Object classification", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image, verbose=0)
    #print(prediction)
    index = np.argmax(prediction)
    print(prediction)
    confidence_score = prediction[0][index]
    if confidence_score >= confidence_threshold:

        if index == 0:
            piece = "Wrench"
        if index == 1:
            piece = "Screwdriver"
        if index == 2:
            piece = "Crank"
        if index == 3:
            piece = "Rod"
        if index == 4:
            piece = "Piston"
        if index == 5:
            piece = "Slider" 
        if index == 6:
            piece = "Blackpillow"     

    else:
        piece = "0"
    os.system("cls")
    print("Pieza: ", piece, " Confidence score: ", confidence_score)

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(10)
    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27 :
        break

camera.release()
cv2.destroyAllWindows()

