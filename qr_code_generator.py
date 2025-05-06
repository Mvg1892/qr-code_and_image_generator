import qrcode

def generate_qr_code(content, file_name):
    qr = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(qr_code_color="black", background_color="white") # here you can change the colors
    img.save(file_name)

# Input Data for the QR-Code
text = "e.g. www.xyz.xy"
# File name and path to save the QR-Code
file_name = "/path/to/qr_code.png"
# generate the QR-Code
generate_qr_code(text, file_name)