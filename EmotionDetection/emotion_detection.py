import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    # Step 1: Convert response text to a dictionary
    response_dict = json.loads(response.text)
    
    # Step 2: Extract the required emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger_score   = emotions['anger']['score']
    disgust_score = emotions['disgust']['score']
    fear_score    = emotions['fear']['score']
    joy_score     = emotions['joy']['score']
    sadness_score = emotions['sadness']['score']
    
    # Step 3: Find the dominant emotion (highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Step 4: Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
