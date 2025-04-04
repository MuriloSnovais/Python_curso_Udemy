# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
IMAGE = ROOT_FOLDER / 'Sung.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(IMAGE)
width, height = pil_image.size
# exif = pil_image.info['exif']

new_width = 640
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width,new_height))

new_image.save(NEW_IMAGE)