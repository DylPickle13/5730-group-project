import os
from feat import Detector

if __name__ == "__main__":
    detector = Detector(emotion_model='svm')
    for root, dirs, files in os.walk("G:\My Drive\School Work\Ontario Tech\Winter 2024\CSCI 5730G\Group Project\RADIATE Color Faces\RADIATE_COLOR_1\AF01"):
        for file in files:
            if file.endswith(".bmp"):
                single_face_prediction = detector.detect_image(os.path.join(root, file))
                print(file)
                print(single_face_prediction.aus)
