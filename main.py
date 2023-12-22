from google_translate import get_credential, google_texts
import time
import os

FILEPATH = 'test.txt'
# 언어코드는 해당 링크 참조
# https://cloud.google.com/translate/docs/languages?hl=ko 
SOURCE = 'ko'
TARGET = 'en'
UNIT = 1024
DELAY = 3

if __name__ == "__main__":
    
    get_credential()
    final_output = []
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
        chunks = [data[i:i+UNIT] for i in range(0, len(data), UNIT)]
    print(f"chunks: {len(chunks)}")
    
    for i, chunk in enumerate(chunks):
        final_output.extend(google_texts(chunk, SOURCE, TARGET))
        print(f"chunk {i+1} done.")
        time.sleep(DELAY)
    
    abspath = os.path.abspath(FILEPATH)
    dir = os.path.dirname(abspath)
    filename = ".".join(os.path.basename(abspath).split('.')[:-1])
    with open(f'{dir}/{filename}_{SOURCE}-{TARGET}.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_output))