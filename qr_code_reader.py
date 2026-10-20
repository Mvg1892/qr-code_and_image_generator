import os
import cv2

def read_qr_code(file_name):
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"File does not exist: {file_name}")

    img = cv2.imread(file_name)
    if img is None:
        raise ValueError(f"File could not be read as an image: {file_name}")

    detector = cv2.QRCodeDetectorAruco()
    data, points, _ = detector.detectAndDecode(img)

    if not data:
        raise ValueError(f"No QR-Code found in: {file_name}")

    return data

if __name__ == "__main__":
    # File name and path of the QR-Code to read, /path/to/qr_code_xxx.png
    file_name = "./qr_code_xxx.png" # current directory where the script is executed
    content = read_qr_code(file_name)
    print(content)
