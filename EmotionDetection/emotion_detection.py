import requests
import json

def emotion_detector(text_to_analyse):
    """
    Emotion Predict function of the Watson NLP Library
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    jsonBody = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=jsonBody, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotion_data = response.json()['emotionPredictions'][0]['emotion']
        scores = {emotion: emotion_data.get(emotion) for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        dominant_emotion = max(scores, key=scores.get)
    elif response.status_code == 400:
        scores = {emotion: None for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        dominant_emotion = None

    return {
        **scores,
        'dominant_emotion': dominant_emotion
    }