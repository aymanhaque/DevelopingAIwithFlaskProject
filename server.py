
from flask import Flask, request
from EmotionDetection import emotion_detection
app = Flask(__name__)

@app.route('/emotionDetector')
def emotionOutput():
    response = request.args.get('textToAnalyze')
    emotions = emotion_detector(response)
    return emotions