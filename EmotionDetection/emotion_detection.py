import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = Input, headers = Headers)
    if(response.status_code == 400):
        Input['raw_document']["text"] = "None"
        response = requests.post(URL, json = Input, headers = Headers)

        errorDict = json.loads(response.text)['emotionPredictions'][0]['emotion']
        for i in errorDict.keys():
            errorDict[i] = None
        errorDict['dominant_emotion'] = None
        return errorDict
    dictionary= json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant = max(dictionary, key = dictionary.get)
    dictionary['dominant_emotion'] = dominant
    

    return dictionary

if(__name__ == "__main__"):
    print(emotion_detector(''))