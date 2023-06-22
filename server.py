import json

import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from flask import Flask, render_template, request
from PIL import Image, ImageChops, ImageOps

app = Flask(__name__)
loaded_model = tf.keras.models.load_model('model')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ImageRecognition', methods=["POST"])
def predict_image():
    img = image.load_img('./img/gambar.png', target_size=(150,150,3))
    #img = Image.open(request.files["gambar"]).convert("L")
    #output = loaded_model.predict(request.files["gambar"])
    #print(output)
    return json.dumps(12)

if __name__ == "__main__":
    app.run(host="0.0.0.0")