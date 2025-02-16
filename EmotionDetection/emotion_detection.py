import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = Input, headers = Headers)
    dictionary= json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant = max(dictionary, key = dictionary.get)
    dictionary['domiant_emotion'] = dominant
    

    return dictionary

print(emotion_detector('I hate working long hours'))