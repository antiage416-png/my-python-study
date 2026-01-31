from pathlib import Path
from step_1_1 import OUT_DIR

data = [
    'BEGIN:VCARD',
    'VERSION:3.0',
    'N:혼자 만들면서 배우는;파이썬;;;',
    'FN:혼자 만들면서 배우는 파이썬',
    'TEL;type=CELL:+82 10-1234-5678',
    'END:VCARD',
]
vcf = '\n'.join(data)
with open(OUT_DIR / f'{Path(__file__).stem}.vcf', 'w',
          encoding='utf-8') as fp:
    fp.write(vcf)

import qrcode

img = qrcode.make(vcf)
img