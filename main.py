import cv2
import numpy as np
import csv
import face_recognition
from datetime import datetime 

video_capture = cv2.VideoCapture(0)

#loading known faces and their encodings

yash_image = face_recognition.load_image_file("images/yash.jpg")
yash_encoding = face_recognition.face_encodings(yash_image)[0]

vishal_image = face_recognition.load_image_file("images/vishal.jpg")    
vishal_encoding = face_recognition.face_encodings(vishal_image)[0]

sanskar_image = face_recognition.load_image_file("images/sanskar.jpg")
sanskar_encoding = face_recognition.face_encodings(sanskar_image)[0]

ritika_image = face_recognition.load_image_file("images/ritika.jpg")
ritika_encoding = face_recognition.face_encodings(ritika_image)[0]

#storing name of encoded faces

known_face_encodings = [yash_encoding, vishal_encoding, sanskar_encoding, ritika_encoding]
known_face_names = ["Yash Pathak", "Vishal Dabi", "Sanskar Gupta", "Ritika Tatawat"]

# list of student in the class who are registered.

students = known_face_names.copy()

face_locations = []
face_encodings = []

#getting current date and time 

current = datetime.now()
current_date = current.strftime("%Y-%m-%d")

#making csv file to store attendance
f =  open(f"Attendance_{current_date}.csv", 'w+', newline='')
csv_writer = csv.writer(f)

while True:
    _, frame = video_capture.read() # returns (True, array([[  0,  23, 255], [ 34,  56, 200], ... ]))
                                    # 3D NumPy array representing the frame's pixels (height × width × color channels)
                                    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # resizing the frame to 1/4th of the original size

    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #locating faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame) #returns list of tuples with coordinates of the face locations in the format (top, right, bottom, left)

    #encoding faces in the frame
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            
            #adding text on the frame
            cv2.rectangle(frame, (face_locations[0][3]*4, face_locations[0][0]*4), (face_locations[0][1]*4, face_locations[0][2]*4), (0, 255, 0), 1 , cv2.LINE_AA)
            
            #adding name on the frame
            cv2.putText(frame, name, (face_locations[0][3]*4 + 5, face_locations[0][0]*4 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)

            if name in students:
                students.remove(name)
                current_time = current.strftime("%H:%M:%S")
                csv_writer.writerow([name, current_time])
                print(f"{name} marked present at {current_time}")   
    
    #displaying the frame
    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

              



