import deepl
from api import API_KEY
DeepL_KEY = API_KEY # 복사한 API 키를 넣으세요.
tran = deepl.Translator(DeepL_KEY)
resp = tran.translate_text('Hello, World',
                           source_lang='EN', target_lang='KO')
resp.text
