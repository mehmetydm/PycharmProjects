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
    labels = ['gerçek', 'sahte']
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
            text = "Bu resim SAHTE."
        elif pred[0] >= 0.6:
            text = "Bu resim GERÇEK."
        else:
            text = "Bu resim GERÇEK ya da SAHTE olabilir."

    else:
        text = "Resimin içinde yüz ifadesi bulunmadı."

    text2 = "GERÇEK: " + str(np.round(pred[0] * 100, 2)) + "%, SAHTE: " + str(np.round(pred[1] * 100, 2)) + "%"

    return input_img, text, text2, {labels[i]: float(pred[i]) for i in range(2)}


title = "Sahte Resim Dedektörü"
description = "Resimlerin sahte olup olmadığını kontrol edebilirsiniz.  "

gr.Interface(deepfakespredict,
             inputs=[gr.inputs.Image(type="pil")],
             outputs=[gr.outputs.Image(type="pil", label="Tespit Edilen Yüz"),
                      "text",
                      "text",
                      gr.outputs.Label(num_top_classes=None, type="auto", label="Eminlik")],
             title=title,
             description=description,
             theme="huggingface"
             ).launch()
