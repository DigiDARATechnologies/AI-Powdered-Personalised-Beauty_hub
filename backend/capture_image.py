import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite('static/captured_image.jpg', frame)
        print("Image captured and saved.")
    else:
        print("Error: Could not read frame.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()