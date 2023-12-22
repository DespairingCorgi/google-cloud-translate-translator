from google_translate import get_credential, google_texts
import time

FILEPATH = 'test.txt'
SOURCE = 'ko'
TARGET = 'en'
UNIT = 1024

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
        time.sleep(3)
        
    with open(f'{FILEPATH}_{SOURCE}-{TARGET}', 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_output))