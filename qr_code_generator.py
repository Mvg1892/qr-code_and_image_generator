import os
import json
import qrcode

def generate_qr_code(content, file_name):
    if not content:
        raise ValueError("content darf nicht leer sein")

    qr = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    directory = os.path.dirname(file_name)
    if directory and not os.path.isdir(directory):
        raise FileNotFoundError(f"Zielordner existiert nicht: {directory}")

    img.save(file_name)

if __name__ == "__main__":
    # Input Data for the QR-Code als JSON, hier Daten einfügen (comma seperated)
    data = {
        "key": "value"
    }
    text = json.dumps(data)
    # File name and path to save the QR-Code, /path/to/qr_code_xxx.png
    file_name = "./qr_code_xxx.png" # aktuelles Verzeichnis wo Skript ausgeführt wird
    # generate the QR-Code
    generate_qr_code(text, file_name)