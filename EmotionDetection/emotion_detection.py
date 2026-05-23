from flask import Flask 
import requests
import json

def emotion_detector(text_to_analyze):
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # for this project we are usinf Emotion Predict function 
    # of the Watson NLP Library
    my_obj= { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL,json=my_obj,headers=Headers)
    if response.status_code==400:
         return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response = json.loads(response.text)
    # print(formatted_response)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    max=0
    dom_emo =''
    # max_value = max(emotion_scores.values())
                    # or
    for j in emotion_scores.keys():
        if max<emotion_scores[j]:
            max=emotion_scores[j]
            dom_emo = j
        else:
            continue

                    # or
    # max_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dom_emo
    print(emotion_scores)

emotion_detector("I love learning")