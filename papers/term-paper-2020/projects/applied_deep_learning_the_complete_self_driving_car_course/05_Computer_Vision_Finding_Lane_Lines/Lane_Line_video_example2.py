import cv2
import numpy as np


def build_canny(image):
    gr = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    bl = cv2.GaussianBlur(gr, (5, 5), 0)
    return cv2.Canny(bl, 50, 150)


def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 200)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, (255, 255, 255))

    return cv2.bitwise_and(image, mask)


def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters

    y1 = image.shape[0]
    y2 = int(y1 * (3 / 5))

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)

    return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):
    left_fit    = []
    right_fit   = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1,x2), (y1,y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope <= 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    left_fit_average  = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line  = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines


def build_hough_lines(image):
    return cv2.HoughLinesP(image,
                    2,
                    np.pi / 180,
                    100,
                    np.array([]),
                    minLineLength = 40,
                    maxLineGap = 5)


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if (lines is not None):
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 15)

    return line_image


def process_frame(frame):
    canny_image = build_canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines = build_hough_lines(cropped_image)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combined_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    return combined_image


video_capture = cv2.VideoCapture("lane_line_video_test.mp4")


while (video_capture.isOpened):
    _, frame = video_capture.read()

    processed_frame = process_frame(frame)
    cv2.imshow("image", processed_frame)
    if cv2.waitKey(1) == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
