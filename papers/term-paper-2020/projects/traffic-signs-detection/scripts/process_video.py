import object_detection as od
import cv2
import time


def process_video(model, video_path, result):
    cap = cv2.VideoCapture(video_path)
    capsize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = cap.get(cv2.CAP_PROP_FPS)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    #fourcc = cv2.VideoWriter_fourcc(*'FMP4')
    #out = cv2.VideoWriter()

    print(capsize)
    print(fps)

    fw = int(cap.get(3))
    fh = int(cap.get(4))
    print("w,h", fw, fh)
    out = cv2.VideoWriter('fb1.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, (fw, fh))


    #success = out.open(result, fourcc, 24, capsize, False)

    counter = 0
    while (cap.isOpened):
        ret, frame = cap.read()
        if ret == True:
            start = time.time()
            processed_frame = od.process_image(model, frame)
            out.write(processed_frame)
            end = time.time()

            counter += 1
            print("Processed: " + str(counter) + " of " + str(length) + " frames. Time elapsed: " + str(end - start))

        else:
            break

        if (counter > 30):
            break

    print("Processed " + str(counter) + " frames!")
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    input_video = "../assets/resources/video/input/small/cars_moscow.mp4"
    output_video = "../assets/resources/video/output/small/cars_moscow.mp4"
    weights_path = "../assets/yolov3.weights"

    model = od.load_model(weights_path)
    process_video(model, input_video, output_video)
