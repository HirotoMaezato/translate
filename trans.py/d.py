import requests
import pprint


translated_text = []

path = 'C:\\Users\\81903\\Desktop\\trans.py\\a.txt'
target_text = []
with open(path,encoding="utf-8_sig") as f:
    target_text = f.readlines()

for l in target_text:

    TEXT = l
    URL = ' https://api-free.deepl.com/v2/translate'
    API_KEY = ''

    params = {
        "auth_key": API_KEY,
        "text": TEXT,
        "source_lang": 'EN', # 入力テキストの言語を日本語に設定（JPではなくJAなので注意）
        "target_lang": 'JA'  # 出力テキストの言語を英語に設定
    }

    r = requests.post(URL, data=params)
    r = r.json()
    translated_text.append(r["translations"][0]["text"])

path_w = 'C:\\Users\\81903\\Desktop\\trans.py\\a_w.txt'

result = [None]*(len(target_text)+len(translated_text))
result[::2] = target_text
result[1::2] = translated_text

with open(path_w,encoding="utf-8_sig", mode='w') as f:
   f.write('\n'.join(result))

print('Finish!!')

