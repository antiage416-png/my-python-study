from pathlib import Path
import qrcode
from step_1_1 import OUT_DIR

img_hello = qrcode.make('헬로, QR 코드!')
img_hello.save(OUT_DIR / f'{Path(__file__).stem}_hello.png')
img_youtube = qrcode.make('https://www.youtube.com/')
img_youtube.save(OUT_DIR / f'{Path(__file__).stem}_youtube.png')