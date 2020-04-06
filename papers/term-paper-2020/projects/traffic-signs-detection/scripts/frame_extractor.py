import cv2
from PIL import Image

source_video = "/Users/almaz/Desktop/PAPER/projects/Traffic-Signal-Violation-Detection-System/Resources/video/input/small/cars_moscow.mp4"
target_folder = "/Users/almaz/Desktop/PAPER/projects/Traffic-Signal-Violation-Detection-System/Resources/images/cars_moscow/"

cap = cv2.VideoCapture(source_video)
frame_number = 0
while (cap.isOpened):
    ret, frame = cap.read()

    if (type(frame) == type(None)):
        break

    if (frame_number % 100 == 0):
        B, R, G = cv2.split(frame)
        fr = cv2.merge([G, R, B])
        im = Image.fromarray(fr)
        file_name = target_folder + str(frame_number) + ".png"
        im.save(file_name, "PNG")
        print(file_name + " Saved")

    frame_number += 1

cap.release()
cv2.destroyAllWindows()