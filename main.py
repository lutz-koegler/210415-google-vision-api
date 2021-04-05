from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import logging
import os.path
import io
import os
from google.cloud import vision
from google.oauth2 import service_account
from faceModel import FaceModel
#from PIL import Image, ImageDraw

#import boto3
#from rekognition_image_detection import RekognitionImage

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1920 * 1920
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def detect():

    # Upload file
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    # Obtain credentials
    credentials = service_account.Credentials.from_service_account_file(
        'My Project-543e6ed386ee.json')

    # Instantiates a client
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # The name of the image file to annotate
    imageToAnnotate_file_name = os.path.join(app.config['UPLOAD_PATH'], filename)

    with io.open(imageToAnnotate_file_name, 'rb') as image_file:
        content = image_file.read()

    # Start face detection
    image = vision.Image(content=content)

    """Detects faces in an image."""
    response = client.face_detection(image=image)
    faces = response.face_annotations

    faceList = []
    for face in faces:
        faceModel = FaceModel(face)
        faceList.append(faceModel)
    return render_template("detect.html", faces=faceList, image=filename);

# start flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)




