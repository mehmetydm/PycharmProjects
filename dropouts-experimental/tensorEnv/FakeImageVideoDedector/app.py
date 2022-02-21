import gradio as gr
import cv2
from mtcnn.mtcnn import MTCNN
import tensorflow as tf
import tensorflow_addons
import numpy as np

import os
import zipfile

local_zip = "FINAL-EFFICIENTNETV2-B0.zip"
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('FINAL-EFFICIENTNETV2-B0')
zip_ref.close()

model = tf.keras.models.load_model("FINAL-EFFICIENTNETV2-B0")

detector = MTCNN()


def deepfakespredict(input_img):
    labels = ['real', 'fake']
    pred = [0, 0]
    text = ""
    text2 = ""

    face = detector.detect_faces(input_img)

    if len(face) > 0:
        x, y, width, height = face[0]['box']
        x2, y2 = x + width, y + height

        cv2.rectangle(input_img, (x, y), (x2, y2), (0, 255, 0), 2)

        face_image = input_img[y:y2, x:x2]
        face_image2 = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        face_image3 = cv2.resize(face_image2, (224, 224))
        face_image4 = face_image3 / 255

        pred = model.predict(np.expand_dims(face_image4, axis=0))[0]

        if pred[1] >= 0.6:
            text = "The image is FAKE."
        elif pred[0] >= 0.6:
            text = "The image is REAL."
        else:
            text = "The image may be REAL or FAKE."

    else:
        text = "Face is not detected in the image."

    text2 = "REAL: " + str(np.round(pred[0] * 100, 2)) + "%, FAKE: " + str(np.round(pred[1] * 100, 2)) + "%"

    return input_img, text, text2, {labels[i]: float(pred[i]) for i in range(2)}


title = "EfficientNetV2 Deepfakes Image Detector"
description = "This is a demo implementation of EfficientNetV2 Deepfakes Image Detector. \
            To use it, simply upload your image, or click one of the examples to load them.  \
            This demo and model represent the Final Year Project titled \"Achieving Face Swapped Deepfakes Detection Using EfficientNetV2\" by a CS undergraduate Lee Sheng Yeh.  \
            The examples were extracted from Celeb-DF(V2)(Li et al, 2020) and FaceForensics++(Rossler et al., 2019). Full reference details is available in \"references.txt.\" \
            The examples are used under fair use to demo the working of the model only. If any copyright is infringed, please contact the researcher via this email: tp054565@mail.apu.edu.my, the researcher will immediately take down the examples used.\
            "

examples = [
    ['Fake-1.png'],
    ['Fake-2.png'],
    ['Fake-3.png'],
    ['Fake-4.png'],
    ['Fake-5.png'],

    ['Real-1.png'],
    ['Real-2.png'],
    ['Real-3.png'],
    ['Real-4.png'],
    ['Real-5.png']

]

gr.Interface(deepfakespredict,
             inputs=["image"],
             outputs=[gr.outputs.Image(type="pil", label="Detected face"),
                      "text",
                      "text",
                      gr.outputs.Label(num_top_classes=None, type="auto", label="Confidence")],
             title=title,
             description=description,
             examples=examples,
             examples_per_page=5
             ).launch()
