from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from step_1_1 import IN_DIR, OUT_DIR
from step_3_2 import OUT_3_2

img_raw = Image.open(OUT_3_2)

text = '발리, 인도네시아' # 이미지에 추가할 메시지
font = ImageFont.truetype(IN_DIR / 'Pretendard-Bold.ttf', size= 100)
left, top, right, bottom = font.getbbox(text)

pad = 20 # 여백
bg_width = pad + right + pad # 메시지 너비에 여백 추가
bg_height = pad + bottom + pad # 메시지 높이에 여백 추가

img_bg = Image.new('RGBA', size=img_raw.size)
draw_bg = ImageDraw.Draw(img_bg)
draw_bg.rectangle(xy=(4000-bg_width,2500-bg_height,4000, 2500), fill=(0,0,0,200))

img_final = Image.alpha_composite(img_raw.convert('RGBA'), img_bg)
draw_final = ImageDraw.Draw(img_final)
draw_final.text(xy=(4000-bg_width,2500-bg_height), text=text, fill=(255,255,255), font=font)

img_final.convert('RGB').save(OUT_DIR/ f'{Path(__file__).stem}.jpg')