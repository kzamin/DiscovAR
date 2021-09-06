import os
import io
from google.cloud import vision
import pandas
import wikipedia

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "GOOGLE_AUTHCODE"  # put your actual AUTH.json here

def detect_landmarks(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations

    landmark = landmarks[0]

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    if(landmark.description.lower() in valid):
        ar = valid[(landmark.description.lower())]
    else:
        ar = "https://go.echoar.xyz/yo8o"

    return [landmark.description, wikipedia.summary(landmark.description), ar]

valid = {"pyramid": "https://go.echoar.xyz/yo8o",
         "space needle": "https://go.echoar.xyz/H98t",
         "taj mahal": "https://go.echoar.xyz/ngvs",
         "stonehenge": "https://go.echoar.xyz/RLdA",
         "eiffel tower": "https://go.echoar.xyz/1SMH"
        }
