import os
from PIL import Image

def generate_image(color, img_size, file_name):
    directory = os.path.dirname(file_name)
    if directory and not os.path.isdir(directory):
        raise FileNotFoundError(f"Target directory does not exist: {directory}")

    img = Image.new("RGB", img_size, color)
    img.save(file_name)

if __name__ == "__main__":
    # Specify color in hex and desired size
    color = "#dce283"
    img_size = (1920, 1080)

    # Save image, file name and path to save the img, /path/to/img.jpg
    file_name = "./1920x1080_dce283.jpg" # current directory where the script is executed
    generate_image(color, img_size, file_name)