#import os
from google.cloud import translate as translate
from google.oauth2 import service_account

#프로젝트 id
PROJECT_ID = "YOURPROJECTID"
#위치 정보
LOCATION = "global"

#디폴트 Source language 정리
#SOURCE_LANG = "en-US"
#디폴트 Target Language 정리
#TARGET_LANG = "ko"
client = None


# 언어코드는 해당 링크 참조
# https://cloud.google.com/translate/docs/languages?hl=ko 



def get_credential():
    '''
        in same scope, you must use this function before you use
        
        translate_text function
        or
        translatte_texts function
    '''
    global credentials
    
    # 해당 모듈과 service_credentials.json이 같은 디렉토리에 있는것을 상정한 상대경로 설정.
    # pycharm 환경 등에서는 절대경로 또는 env에 추가하여 사용할 것을 권장.
    credentials = service_account.Credentials.from_service_account_file('./service_credentials.json')

# Initialize Translation client
def google_text(text, source_lang='ko', target_lang='en', bePararell=False):
    
    '''
        this function translates and return a text
        
        input:
        
        text -> String : text to translate
        bePararell -> Bool : determines the output would be pararell or not
        source_lang -> String(optional) : source language code (default: SOURCE_LANG)
        target_lang -> String(optional) : target language code (default: TARGET_LANG)
    
        output:
        
        if bePararell == False -> text : translated text
        if bePararell == True -> Tuple<String, String> : pair of original text and translated text
        
    '''

    global credentials
    global client
    if not client:
        client = translate.TranslationServiceClient(credentials=credentials)
    parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_lang,
            "target_language_code": target_lang,
        }
    )

    #print("Translated text: {}".format(response.translations[0].translated_text))
    
    if bePararell:
       return (text, response.translations[0].translated_text) 
    return response.translations[0].translated_text
        

def google_texts(texts, source_lang='ko', target_lang='en', bePararell=False):
    
    '''
        this function translates and return a list of text
        
        input:
        
        text -> List<String> : text to translate
        bePararell -> Bool : determines would be pararell or not
        source_lang -> String : source language code (default: SOURCE_LANG)
        target_lang -> String : target language code (default: TARGET_LANG)
        
        output:
        
        if bePararell == False -> text : translated text
        if bePararell == True -> List<Tuple<String, String>> : pair of original text and translated text
    '''
    
    global credentials
    global client
    if client==None:
        client = translate.TranslationServiceClient(credentials=credentials)
    parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": texts,
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_lang,
            "target_language_code": target_lang,
        }
    )

    # for translation in response.translations:
    #     print("Translated text: {}".format(translation.translated_text))
        
    if bePararell:
        return list(zip(texts, list(x.translated_text for x in response.translations)))
    return list(x.translated_text for x in response.translations)

# get_credential()
# print(google_texts(['안녕하시오!', '잘 가시게나!'], 'ko', 'de'))
