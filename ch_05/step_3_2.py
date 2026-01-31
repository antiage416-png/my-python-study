from pathlib import Path
import deepl
from step_1 import IN_DIR
from step_2_2 import read_text
from api import API_KEY

def read_text_translated(path: Path) -> list:
    text_list = read_text(path) # 문자 인식 함수
    DeepL_KEY = API_KEY # DEEPL_KEY
    tran = deepl.Translator(DeepL_KEY)
    result = []
    for coords, text, prob in text_list:
        resp = tran.translate_text(text, target_lang='KO')
        result.append((coords, resp.text, prob))
    return result

if __name__ == '__main__':
    path = IN_DIR / 'ocr.jpg'
    print(read_text_translated(path))