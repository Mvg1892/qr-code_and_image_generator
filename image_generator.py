from PIL import Image

# Specify color in hex and desired size
color = "#dce283"
img_size = (1920, 1080)

# Create new image
img = Image.new("RGB", img_size, color)

# Save image
storage_location = "/path/to/1920x1080_dce283.jpg"
img.save(storage_location)