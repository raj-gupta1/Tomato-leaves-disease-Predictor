from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='model_VGG19_best.h5'

# Loading the trained model
model = load_model(MODEL_PATH)

# your_model = tf.keras.models.load_model(
#     path_to_h5,
#     custom_objects={'Functional':tf.keras.models.Model})


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)

    ## Scaling
    x = x/255
    x = np.expand_dims(x, axis=0)
   

   

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds == 0:
        preds="Bacterial_spot"
    elif preds == 1:
        preds="Early_blight"
    elif preds == 2:
        preds="Late_blight"
    elif preds == 3:
        preds="Leaf Mold"
    elif preds == 4:
        preds = "Septoria leaf spot"
    elif preds == 5:
        preds = "Spider mites (Two spotted spider mite)"
    elif preds == 6:
        preds = "Target_Spot"
    elif preds == 7:
        preds="Yellow_Leaf_Curl_Virus"
    elif preds == 8:
        preds = "Mosaic_virus"
    else:
        preds="No worries. Your plant is healthy."

    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result = preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
