import cv2
import pickle
import numpy as np
import os
import sys
import time

# Video capturing using webcam
video = cv2.VideoCapture(0)

# Adding face detection algorithm (predefined)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
faces_data = []
i = 0

if not os.path.exists('data'):
    os.makedirs('data')

name = input("Enter your Name: ")
reg_no = input("Enter your Reg no: ")

def check_reg_no_exists(reg_no, file_path='data/names_and_rolls.txt'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if reg_no in line.split(',')[1].strip():
                    print("Registration number already exists. Exiting...")
                    time.sleep(2)
                    sys.exit()
    return 0

checking_reg_no_exist = check_reg_no_exists(reg_no)
if checking_reg_no_exist == 0:
    while True:
        ret, frame = video.read()

        # Converting to greyscale for better face detection
        greyscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = facedetect.detectMultiScale(greyscale, 1.3, 5)

        for (x, y, w, h) in faces:
            crop_img = frame[y:y+h, x:x+w, :]
            resize_img = cv2.resize(crop_img, (50, 50))

            if len(faces_data) < 100 and i % 10 == 0:
                faces_data.append(resize_img)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

        i += 1
        # Drawing rectangle and displaying texts
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.putText(frame, "Recording face, please wait", (0, 400), cv2.FONT_HERSHEY_TRIPLEX, 1, (50, 50, 255), 1)
        cv2.putText(frame, "util count become 100", (0, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (50, 50, 255), 1)
        cv2.putText(frame, "press 'Q' to exit", (5, 0), cv2.FONT_ITALIC, 1, (50, 50, 255), 1)

        # Showing the webcam 
        cv2.imshow("Frame", frame)
        

        # Quit cam while pressing 'q' or when 100 images are collecqqted
        k = cv2.waitKey(1)
        
        if k == ord('q'):
            break

        if len(faces_data) == 100:
            print("Image captured successfully.")
            with open('data/names_and_rolls.txt', 'a') as f:
                f.write(f"{name},{reg_no}\n")
            break

video.release()
cv2.destroyAllWindows()

if len(faces_data) == 100:
    faces_data = np.asarray(faces_data)
    faces_data = faces_data.reshape(len(faces_data), -1)  # Ensure correct shape

    # Save or append the name data
    if 'names.pkl' not in os.listdir('data/'):
        names = [name] * 100
        with open('data/names.pkl', 'wb') as f:
            pickle.dump(names, f)
    else:
        with open('data/names.pkl', 'rb') as f:
            names = pickle.load(f)
        names.extend([name] * 100)
        with open('data/names.pkl', 'wb') as f:
            pickle.dump(names, f)

    # Save or append the face data
    if 'faces_data.pkl' not in os.listdir('data/'):
        with open('data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces_data, f)
    else:
        with open('data/faces_data.pkl', 'rb') as f:
            faces = pickle.load(f)
        faces = np.append(faces, faces_data, axis=0)
        with open('data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces, f)
else:
    print("No faces were captured. Please try again.")
