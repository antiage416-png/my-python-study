from PIL import Image
from step_1_1 import IMG_DIR

img = Image.open(IMG_DIR / 'img_001.jpg')
img

from PIL import ImageDraw
draw= ImageDraw.Draw(img)
draw.text(
    xy=(150,1000),
    text='Hello World',
    fill=(255,255,255),
    font_size=100,
)

img