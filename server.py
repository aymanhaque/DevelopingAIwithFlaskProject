from flask import Flask, request
from EmotionDetection import emotion_detection
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/emotionDetector')
def emotionOutput():
    response = request.args.get('textToAnalyze')
    emotions = emotion_detection.emotion_detector(response)
    statement = f"""For the given statement, the system response is 
        'anger': {emotions['anger']}, 
        'disgust':{emotions['disgust']}, 
        'fear': {emotions['fear']}, 
        'joy': {emotions['joy']}, 
        and 
        'sadness': {emotions['sadness']}. 
        The dominant emotion is {emotions['dominant_emotion']}.
        """
    return statement