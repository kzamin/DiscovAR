import os
import io
from google.cloud import vision
import pandas
import wikipedia

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "GOOGLE_AUTH_CODE"  # put your actual AUTH.json here

# file_name = input("Enter file name:")
# image_path = 'Images/' + file_name

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

    print(landmark.description, wikipedia.summary(landmark.description))
    result = ["hello", "world"]
    result = [landmark.description, wikipedia.summary(landmark.description)]
    return result
    
# landmark = detect_landmarks(image_path)
# print(landmark.description)
#
# valid = {"Pyramid": "https://go.echoar.xyz/yo8o",
#          "Space Needle": "https://go.echoar.xyz/H98t",
#          "Stonehenge":"https://console.echoar.xyz/samples/webar-chrome/snowy-firefly-0544_1602992125554/index_snowy-firefly-0544_1602992125554.html",
#          "Eiffel Tower": "https://console.echoar.xyz/samples/webar-chrome/snowy-firefly-0544_1602992178975/index_snowy-firefly-0544_1602992178975.html",
#          "Taj Mahal": "https://console.echoar.xyz/samples/webar-chrome/snowy-firefly-0544_1602992216830/index_snowy-firefly-0544_1602992216830.html",
#          "New York City": "https://console.echoar.xyz/samples/webar-chrome/snowy-firefly-0544_1602992277351/index_snowy-firefly-0544_1602992277351.html",
#          "Colosseum": "https://console.echoar.xyz/samples/webar-chrome/snowy-firefly-0544_1602992324002/index_snowy-firefly-0544_1602992324002.html"}
#
# print("Wikipedia Summary")
# print(wikipedia.summary(landmark.description))
# print(valid.get(landmark.description))