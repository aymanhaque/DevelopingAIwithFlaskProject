from flask import Flask, request, abort
from EmotionDetection import emotion_detection
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/emotionDetector')
def emotionOutput():
    response = request.args.get('textToAnalyze')
    if response =="":
        abort(400)
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

@app.errorhandler(400)
def bad_request(e):
    return "Invalid request. Please check your input.", 400